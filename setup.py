from cx_Freeze import setup, Executable
import sys

# تنظیمات اضافی
build_exe_options = {
    "packages": ["tkinter", "geopy", "timezonefinder", "requests", "pytz"],  # لیست پکیج‌ها
    "include_files": ["search.png", "search_icon.png", "logo.png", "box.png"]  # فایل‌های اضافی
}

# تنظیمات اصلی
setup(
    name = "Weather App",  # نام برنامه
    version = "1.0",  # نسخه برنامه
    description = "A weather application.",  # توضیحات برنامه
    options = {"build_exe": build_exe_options},  # تنظیمات اضافی
    executables = [Executable("weather.py", base="Win32GUI")]  # فایل پایتون و تنظیم base برای جلوگیری از باز شدن کنسول
)
