import streamlit as st

# Set app title and creator name
st.title("📏 Ultimate Unit Converter")
st.markdown("Convert any unit with ease! 🚀")
st.markdown("**Created by Muneeb Ahmed**")

# Sidebar for additional options
st.sidebar.header("Settings")
theme = st.sidebar.selectbox("Choose Theme", ["Light", "Dark", "Blue", "Green"])

# Apply theme
if theme == "Dark":
    st.markdown(
        """
        <style>
        .stApp {
            background-color: #1E1E1E;
            color:rgb(76, 175, 152);
        }
        h1, h2, h3, h4, h5, h6 {
            color: #FFFFFF;
        }
        .stSelectbox, .stTextInput, .stNumberInput {
            background-color:rgb(100, 131, 255);
            color: #FFFFFF;
        }
        .stButton button {
            background-color: #4CAF50;
            color: white;
            font-size: 16px;
            padding: 10px 24px;
            border-radius: 8px;
        }
        .stButton button:hover {
            background-color: #45a049;
        }
        .sidebar .sidebar-content {
            background-color: #1E1E1E;
            color: #FFFFFF;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
elif theme == "Blue":
    st.markdown(
        """
        <style>
        .stApp {
            background-color: #E6F7FF;
            color: #003366;
        }
        h1, h2, h3, h4, h5, h6 {
            color: #003366;
        }
        .stSelectbox, .stTextInput, .stNumberInput {
            background-color: #FFFFFF;
            color: #003366;
        }
        .stButton button {
            background-color: #0077B6;
            color: white;
            font-size: 16px;
            padding: 10px 24px;
            border-radius: 8px;
        }
        .stButton button:hover {
            background-color: #005F8C;
        }
        .sidebar .sidebar-content {
            background-color: #E6F7FF;
            color: #003366;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
elif theme == "Green":
    st.markdown(
        """
        <style>
        .stApp {
            background-color: #E6FFE6;
            color: #006400;
        }
        h1, h2, h3, h4, h5, h6 {
            color: #006400;
        }
        .stSelectbox, .stTextInput, .stNumberInput {
            background-color: #FFFFFF;
            color: #006400;
        }
        .stButton button {
            background-color: #4CAF50;
            color: white;
            font-size: 16px;
            padding: 10px 24px;
            border-radius: 8px;
        }
        .stButton button:hover {
            background-color: #45a049;
        }
        .sidebar .sidebar-content {
            background-color: #E6FFE6;
            color: #006400;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
else:
    st.markdown(
        """
        <style>
        .stApp {
            background-color: #FFFFFF;
            color: #000000;
        }
        h1, h2, h3, h4, h5, h6 {
            color: #000000;
        }
        .stSelectbox, .stTextInput, .stNumberInput {
            background-color: #FFFFFF;
            color: #000000;
        }
        .stButton button {
            background-color: #4CAF50;
            color: white;
            font-size: 16px;
            padding: 10px 24px;
            border-radius: 8px;
        }
        .stButton button:hover {
            background-color: #45a049;
        }
        .sidebar .sidebar-content {
            background-color: #FFFFFF;
            color: #000000;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

# Conversion factors for all categories
conversion_factors = {
    "Length": {
        "Meters": 1,
        "Kilometers": 0.001,
        "Centimeters": 100,
        "Millimeters": 1000,
        "Inches": 39.3701,
        "Feet": 3.28084,
        "Yards": 1.09361,
        "Miles": 0.000621371,
        "Nautical Miles": 0.000539957,
        "Micrometers": 1e6,
        "Nanometers": 1e9,
        "Angstroms": 1e10,
        "Fathoms": 0.546807,
        "Furlongs": 0.00497096,
        "Light Years": 1.057e-16,
        "Parsecs": 3.24078e-17,
        "Dekameters": 0.1,
        "Hectometers": 0.01,
        "Megameters": 1e-6,
        "Gigameters": 1e-9,
        "Terameters": 1e-12,
        "Petameters": 1e-15,
        "Exameters": 1e-18,
        "Zeptometers": 1e21,
        "Yoctometers": 1e24,
        "Attometers": 1e18,
        "Femtometers": 1e15,
        "Picometers": 1e12,
        "Microns": 1e6,
        "Decimeters": 10,
        "Yottameters": 1e-24,
        "Leagues": 0.000207124,
        "Chains": 0.0497097,
        "Rods": 0.198839,
        "Smoots": 0.587613,
        "Cubits": 2.18723,
        "Beard Seconds": 1e10,
        "Astronomical Units": 6.68459e-12,
        "Marathons": 0.0000235156,
        "Half Marathons": 0.0000470312,
        "Li": 0.002,
        "Mil": 39370.1,
        "Nautical Miles (UK)": 0.000539612,
        "Megafurlongs": 0.00000497096,
        "Kiloparsecs": 3.24078e-20,
        "Megaparsecs": 3.24078e-23,
        "Gigaparsecs": 3.24078e-26,
        "Teraparsecs": 3.24078e-29,
    },
    "Mass": {
        "Kilograms": 1,
        "Grams": 1000,
        "Milligrams": 1e6,
        "Pounds": 2.20462,
        "Ounces": 35.274,
        "Stones": 0.157473,
        "Metric Tons": 0.001,
        "Carats": 5000,
        "Atomic Mass Units": 6.022e26,
        "Slugs": 0.0685218,
    },
    "Temperature": {
        "Celsius": 1,
        "Fahrenheit": 33.8,
        "Kelvin": 274.15,
        "Rankine": 493.47,
    },
    "Speed": {
        "Meters/Second": 1,
        "Kilometers/Hour": 3.6,
        "Miles/Hour": 2.23694,
        "Feet/Second": 3.28084,
        "Knots": 1.94384,
        "Mach": 0.00293858,
        "Speed of Light": 3.3356e-9,
    },
    "Volume": {
        "Liters": 1,
        "Milliliters": 1000,
        "Gallons": 0.264172,
        "Quarts": 1.05669,
        "Pints": 2.11338,
        "Cubic Meters": 0.001,
        "Cubic Feet": 0.0353147,
        "Cubic Inches": 61.0237,
        "Cubic Yards": 0.00130795,
        "Fluid Ounces": 33.814,
        "US bushel": 0.0283776,
        "US peck": 0.11351,
        "US dry gallon": 0.22702,
        "US gallon": 0.264172,
        "US dry quart": 1.10122,
        "US quart": 1.05669,
        "US dry pint": 2.20244,
        "US pint": 2.11338,
        "US cup": 4.22675,
        "US ounce": 33.814,
        "US tablespoon": 67.628,
        "US teaspoon": 202.884,
        "US gill": 8.45351,
        "US beer barrel": 0.00852168,
        "Oil barrel": 0.00628981,
        "Imperial bushel": 0.0283776,
        "Imperial peck": 0.11351,
        "Imperial gallon": 0.219969,
        "Imperial quart": 0.879877,
        "Imperial pint": 1.75975,
        "Imperial ounce": 35.1951,
        "Imperial tbsp.": 56.3121,
        "Imperial tsp.": 168.936,
        "Nanoliter": 1e9,
        "Microliter": 1e6,
        "Milliliter": 1000,
        "Centiliter": 100,
        "Deciliter": 10,
        "Decaliter": 0.1,
        "Hectoliter": 0.01,
        "Kiloliter": 0.001,
        "Megaliter": 1e-6,
        "Cubic nanometer": 1e27,
        "Cubic millimeter": 1e9,
        "Cubic centimeter": 1e6,
        "Cubic decimeter": 1000,
        "Cubic meter": 1,
        "Cubic kilometer": 1e-9,
        "Cubic foot": 0.0353147,
        "Cubic inch": 61.0237,
        "Cubic yard": 0.00130795,
        "Cubic mile": 2.39913e-10,
        "Cubic rod": 0.000207124,
        "Cord": 0.000275896,
        "Hogshead": 0.000419321,
    },
    "Area": {
        "Square Meters": 1,
        "Square Kilometers": 1e-6,
        "Square Centimeters": 10000,
        "Square Millimeters": 1e6,
        "Square Inches": 1550,
        "Square Feet": 10.7639,
        "Square Yards": 1.19599,
        "Acres": 0.000247105,
        "Hectares": 0.0001,
        "Square Miles": 3.861e-7,
        "Hectare": 0.0001,
        "Are": 0.01,
        "Square decimeter": 100,
        "Square rod": 0.0395369,
        "Rood": 0.000988422,
        "Barn": 1e28,
    },
    "Time": {
        "Seconds": 1,
        "Minutes": 1 / 60,
        "Hours": 1 / 3600,
        "Days": 1 / 86400,
        "Weeks": 1 / 604800,
        "Months": 1 / 2.628e6,
        "Years": 1 / 3.154e7,
        "Decades": 1 / 3.154e8,
        "Centuries": 1 / 3.154e9,
        "Femtosecond": 1e15,
        "Picosecond": 1e12,
        "Nanosecond": 1e9,
        "Microsecond": 1e6,
        "Millisecond": 1000,
        "Fortnight": 1 / 1209600,
        "Sidereal year": 1 / 3.15576e7,
        "Millennium": 1 / 3.154e10,
    },
    "Frequency": {
        "Hertz": 1,
        "Kilohertz": 1e-3,
        "Megahertz": 1e-6,
        "Gigahertz": 1e-9,
        "Terahertz": 1e-12,
        "Microhertz": 1e6,
        "Millihertz": 1000,
        "Petahertz": 1e-15,
        "Exahertz": 1e-18,
    },
    "Angle": {
        "Degrees": 1,
        "Radians": 0.0174533,
        "Gradians": 1.11111,
        "Milliradian": 1000,
        "Microradian": 1e6,
        "Revolution": 0.00277778,
        "Arc minute": 60,
        "Arc second": 3600,
        "Milliarcsecond": 3.6e6,
        "Microarcsecond": 3.6e9,
    },
    "Force": {
        "Newtons": 1,
        "Kilonewtons": 1e-3,
        "Pounds-Force": 0.224809,
        "Dynes": 1e5,
        "Gram-force": 101.972,
        "Ounce-force": 3.59694,
        "Kilogram-force": 0.101972,
        "Kip-force": 0.000224809,
        "Metric ton-force": 0.000101972,
    },
    "Pressure": {
        "Pascals": 1,
        "Kilopascals": 1e-3,
        "Atmospheres": 9.86923e-6,
        "Bars": 1e-5,
        "PSI": 0.000145038,
        "Torr": 0.00750062,
        "Barve": 1e-5,
        "Millipascal": 1000,
        "Hectopascal": 0.01,
        "Megapascal": 1e-6,
        "Gigapascal": 1e-9,
        "Technical atmosphere": 0.0000101972,
        "Millibar": 0.01,
        "Centibar": 0.1,
        "Decibar": 0.01,
        "Kilobar": 1e-8,
        "Megabar": 1e-11,
        "Gigabar": 1e-14,
    },
    "Energy": {
        "Joules": 1,
        "Kilojoules": 1e-3,
        "Calories": 0.239006,
        "Kilocalories": 0.000239006,
        "Electronvolts": 6.242e18,
        "BTU": 0.000947817,
        "Erg": 1e7,
        "Foot pound": 0.737562,
        "Decielectron volt": 6.242e19,
        "Centielectron volt": 6.242e20,
        "Millielectron volt": 6.242e21,
        "Microelectron volt": 6.242e24,
        "Nanoelectron volt": 6.242e27,
        "Picoelectron volt": 6.242e30,
        "Femtoelectron volt": 6.242e33,
        "Attoelectron volt": 6.242e36,
        "Zeptoelectron volt": 6.242e39,
        "Yoctoelectron volt": 6.242e42,
        "Decaelectron volt": 6.242e17,
        "Hectoelectron volt": 6.242e16,
        "Kiloelectron volt": 6.242e15,
        "Megaelectron volt": 6.242e12,
        "Gigaelectron volt": 6.242e9,
        "Teraelectron volt": 6.242e6,
        "Petaelectron volt": 6.242e3,
        "Exaelectron volt": 6.242,
        "Zettaelectron volt": 6.242e-3,
        "Yottaelectron volt": 6.242e-6,
    },
    "Power": {
        "Watts": 1,
        "Kilowatts": 1e-3,
        "Horsepower": 0.00134102,
        "Megawatts": 1e-6,
        "Gigawatt": 1e-9,
        "Terawatt": 1e-12,
        "Petawatt": 1e-15,
        "Exawatt": 1e-18,
    },
    "Electric Current": {
        "Amperes": 1,
        "Milliamperes": 1000,
        "Kiloamperes": 1e-3,
        "Microampere": 1e6,
        "Megaampere": 1e-6,
        "Gigaampere": 1e-9,
        "Teraampere": 1e-12,
        "Petaampere": 1e-15,
        "Exaampere": 1e-18,
    },
    "Voltage": {
        "Volts": 1,
        "Millivolts": 1000,
        "Kilovolts": 1e-3,
        "Microvolt": 1e6,
        "Megavolt": 1e-6,
        "Gigavolt": 1e-9,
        "Teravolt": 1e-12,
        "Petavolt": 1e-15,
        "Exavolt": 1e-18,
    },
    "Resistance": {
        "Ohms": 1,
        "Kiloohms": 1e-3,
        "Megaohms": 1e-6,
        "Microohm": 1e6,
        "Milliohm": 1000,
    },
    "Digital Storage": {
        "Bytes": 1,
        "Kilobytes": 1e-3,
        "Megabytes": 1e-6,
        "Gigabytes": 1e-9,
        "Terabytes": 1e-12,
        "Petabytes": 1e-15,
        "Bit": 8,
        "Nibble": 2,
        "Kilobit": 8e-3,
        "Kibibit": 8.192e-3,
        "Kilobyte": 1e-3,
        "Kibibyte": 1.024e-3,
        "Megabit": 8e-6,
        "Mebibit": 8.389e-6,
        "Megabyte": 1e-6,
        "Mebibyte": 1.049e-6,
        "Gigabit": 8e-9,
        "Gibibit": 8.59e-9,
        "Gigabyte": 1e-9,
        "Gibibyte": 1.074e-9,
        "Terabit": 8e-12,
        "Tebibit": 8.796e-12,
        "Terabyte": 1e-12,
        "Tebibyte": 1.1e-12,
        "Petabit": 8e-15,
        "Pebibit": 9.007e-15,
        "Petabyte": 1e-15,
        "Pebibyte": 1.126e-15,
        "Exabit": 8e-18,
        "Exbibit": 9.223e-18,
        "Exabyte": 1e-18,
        "Exbibyte": 1.153e-18,
        "Zettabit": 8e-21,
    },
    "Fuel Consumption": {
        "Kilometers/Liter": 1,
        "Miles/Gallon": 2.35215,
        "Liters/100 Kilometers": 100,
        "MPG (US)": 2.35215,
        "MPG (Imp.)": 2.82481,
    },
}

# Dropdown for category selection
category = st.selectbox("Select Category", list(conversion_factors.keys()))

# Search bar for units
search_unit = st.text_input("Search for a unit")

# Filter units based on search
filtered_units = [unit for unit in conversion_factors[category].keys() if search_unit.lower() in unit.lower()]

# Columns for unit selection
col1, col2 = st.columns(2)
with col1:
    from_unit = st.selectbox("From", filtered_units)
with col2:
    to_unit = st.selectbox("To", filtered_units)

# Input for value
value = st.number_input("Enter value", min_value=0.0, format="%f")

# Conversion function
def convert_units(value, from_unit, to_unit, category):
    if category == "Temperature":
        if from_unit == "Celsius" and to_unit == "Fahrenheit":
            return (value * 9/5) + 32
        elif from_unit == "Fahrenheit" and to_unit == "Celsius":
            return (value - 32) * 5/9
        elif from_unit == "Celsius" and to_unit == "Kelvin":
            return value + 273.15
        elif from_unit == "Kelvin" and to_unit == "Celsius":
            return value - 273.15
        elif from_unit == "Fahrenheit" and to_unit == "Kelvin":
            return (value - 32) * 5/9 + 273.15
        elif from_unit == "Kelvin" and to_unit == "Fahrenheit":
            return (value - 273.15) * 9/5 + 32
        else:
            return value
    else:
        factor_from = conversion_factors[category][from_unit]
        factor_to = conversion_factors[category][to_unit]
        return value * (factor_to / factor_from)

# Real-time conversion
if value:
    result = convert_units(value, from_unit, to_unit, category)
    st.success(f"Converted value: **{result:.4f} {to_unit}**")

    # Copy to clipboard functionality
    if st.button("Copy to Clipboard"):
        st.code(f"{result:.4f} {to_unit}", language="text")
        st.write("Manually copy the value from above.")

# Formula Display
st.markdown("---")
st.subheader("Conversion Formula")

if value:  # Check if value is provided
    if category == "Temperature":
        if from_unit == "Celsius" and to_unit == "Fahrenheit":
            st.write(f"**Formula**: ({value} × 9/5) + 32 = {result:.4f}")
        elif from_unit == "Fahrenheit" and to_unit == "Celsius":
            st.write(f"**Formula**: ({value} - 32) × 5/9 = {result:.4f}")
        elif from_unit == "Celsius" and to_unit == "Kelvin":
            st.write(f"**Formula**: {value} + 273.15 = {result:.4f}")
        elif from_unit == "Kelvin" and to_unit == "Celsius":
            st.write(f"**Formula**: {value} - 273.15 = {result:.4f}")
        elif from_unit == "Fahrenheit" and to_unit == "Kelvin":
            st.write(f"**Formula**: ({value} - 32) × 5/9 + 273.15 = {result:.4f}")
        elif from_unit == "Kelvin" and to_unit == "Fahrenheit":
            st.write(f"**Formula**: ({value} - 273.15) × 9/5 + 32 = {result:.4f}")
    else:
        factor_from = conversion_factors[category][from_unit]
        factor_to = conversion_factors[category][to_unit]
        st.write(f"**Formula**: {value} × ({factor_to} / {factor_from}) = {result:.4f}")
else:
    st.write("**Formula**: Enter a value to see the conversion formula.")

# History of conversions
if "history" not in st.session_state:
    st.session_state.history = []

if st.button("Add to History"):
    st.session_state.history.append(
        f"{value} {from_unit} = {result:.4f} {to_unit}"
    )

if st.session_state.history:
    st.markdown("---")
    st.subheader("Conversion History")
    for entry in st.session_state.history:
        st.write(entry)

# Basic Unit Conversion Chart
st.markdown("---")
st.subheader("Basic Unit Conversion Chart")
if category == "Length":
    st.write("1 Meter = 100 Centimeters = 1000 Millimeters = 39.3701 Inches = 3.28084 Feet = 1.09361 Yards = 0.000621371 Miles")
elif category == "Mass":
    st.write("1 Kilogram = 1000 Grams = 1e6 Milligrams = 2.20462 Pounds = 35.274 Ounces")
elif category == "Temperature":
    st.write("Celsius to Fahrenheit: (C × 9/5) + 32")
    st.write("Fahrenheit to Celsius: (F - 32) × 5/9")
    st.write("Celsius to Kelvin: C + 273.15")
    st.write("Kelvin to Celsius: K - 273.15")
elif category == "Speed":
    st.write("1 Meter/Second = 3.6 Kilometers/Hour = 2.23694 Miles/Hour = 3.28084 Feet/Second = 1.94384 Knots")
elif category == "Volume":
    st.write("1 Liter = 1000 Milliliters = 0.264172 Gallons = 1.05669 Quarts = 2.11338 Pints")
elif category == "Area":
    st.write("1 Square Meter = 10000 Square Centimeters = 1e6 Square Millimeters = 1550 Square Inches = 10.7639 Square Feet = 1.19599 Square Yards = 0.000247105 Acres")
elif category == "Time":
    st.write("1 Second = 1/60 Minutes = 1/3600 Hours = 1/86400 Days = 1/604800 Weeks = 1/2.628e6 Months = 1/3.154e7 Years")
elif category == "Frequency":
    st.write("1 Hertz = 1e-3 Kilohertz = 1e-6 Megahertz = 1e-9 Gigahertz")
elif category == "Angle":
    st.write("1 Degree = 0.0174533 Radians = 1.11111 Gradians")
elif category == "Force":
    st.write("1 Newton = 1e-3 Kilonewtons = 0.224809 Pounds-Force")
elif category == "Pressure":
    st.write("1 Pascal = 1e-3 Kilopascals = 9.86923e-6 Atmospheres = 1e-5 Bars = 0.000145038 PSI")
elif category == "Energy":
    st.write("1 Joule = 1e-3 Kilojoules = 0.239006 Calories = 0.000239006 Kilocalories = 6.242e18 Electronvolts")
elif category == "Power":
    st.write("1 Watt = 1e-3 Kilowatts = 0.00134102 Horsepower")
elif category == "Electric Current":
    st.write("1 Ampere = 1000 Milliamperes = 1e-3 Kiloamperes")
elif category == "Voltage":
    st.write("1 Volt = 1000 Millivolts = 1e-3 Kilovolts")
elif category == "Resistance":
    st.write("1 Ohm = 1e-3 Kiloohms = 1e-6 Megaohms")
elif category == "Digital Storage":
    st.write("1 Byte = 1e-3 Kilobytes = 1e-6 Megabytes = 1e-9 Gigabytes = 1e-12 Terabytes")
elif category == "Fuel Consumption":
    st.write("1 Kilometer/Liter = 2.35215 Miles/Gallon = 100 Liters/100 Kilometers")