# weather app using kivy framework
import requests
import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


def get_weather_data(city):
    city = (city or "").strip()
    if not city:
        raise ValueError("City name is required.")

    api_key = "dfad3e7e41299f77cb5c369b2f2aa572"
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {"q": city, "appid": api_key, "units": "metric"}

    response = requests.get(base_url, params=params, timeout=10)
    response.raise_for_status()
    return response.json()


def main():
    city = input("Enter city name: ")
    try:
        weather_data = get_weather_data(city)
        print(weather_data)
    except Exception as exc:
        print(f"Error: {exc}")


# kivy interface code

class WeatherApp(App):
    def build(self):
        self.title = "Weather App"
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        self.city_input = TextInput(
            hint_text="Enter city name",
            multiline=False,
            size_hint=(1, 0.2)
        )
        self.city_input.bind(on_text_validate=self.get_weather)
        layout.add_widget(self.city_input)

        self.get_weather_button = Button(text="Get Weather", size_hint=(1, 0.2))
        self.get_weather_button.bind(on_press=self.get_weather)
        layout.add_widget(self.get_weather_button)

        self.weather_label = Label(
            text="Enter a city to get the weather.",
            size_hint=(1, 0.6),
            halign="center",
            valign="middle",
            text_size=(self.width, None)
        )
        layout.add_widget(self.weather_label)

        return layout

    def get_weather(self, instance):
        city = self.city_input.text
        if not city.strip():
            self.weather_label.text = "Please enter a city name."
            return

        try:
            weather_data = get_weather_data(city)
            if weather_data.get("cod") == 200:
                temp_c = weather_data["main"]["temp"]
                description = weather_data["weather"][0]["description"].title()
                self.weather_label.text = (
                    f"Temperature: {temp_c:.1f}°C\n"
                    f"Description: {description}"
                )
            else:
                self.weather_label.text = "City not found. Please try again."
        except requests.RequestException:
            self.weather_label.text = "Network error. Please try again later."
        except ValueError:
            self.weather_label.text = "Please enter a city name."
        except Exception:
            self.weather_label.text = "Unable to fetch weather data."

if __name__ == "__main__":
    WeatherApp().run()

