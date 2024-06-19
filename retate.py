from PIL import Image
import os

# Создание папок для сохранения повернутых изображений
output_folder_90 = r"E:\game\гблоки\90"
output_folder_180 = r"E:\game\гблоки\180"
output_folder_270 = r"E:\game\гблоки\270"
os.makedirs(output_folder_90, exist_ok=True)
os.makedirs(output_folder_180, exist_ok=True)
os.makedirs(output_folder_270, exist_ok=True)

input_folder = r"E:\game\гблоки\0"
# Перебор всех файлов в папке

for file_name in os.listdir(input_folder):
    # Проверка, что файл является изображением
    if file_name.endswith(".png") or file_name.endswith(".jpg"):
        # Полный путь к исходному файлу
        input_path = os.path.join(input_folder, file_name)
        
        # Открытие исходного изображения
        original_image = Image.open(input_path)
        
        # Поворот на 90 градусов
        rotated_image_90 = original_image.rotate(90)
        # Сохранение повернутого изображения
        output_path_90 = os.path.join(output_folder_90, file_name)
        rotated_image_90.save(output_path_90)
        
        # Поворот на 180 градусов
        rotated_image_180 = original_image.rotate(180)
        # Сохранение повернутого изображения
        output_path_180 = os.path.join(output_folder_180, file_name)
        rotated_image_180.save(output_path_180)
        
        # Поворот на 270 градусов
        rotated_image_270 = original_image.rotate(270)
        # Сохранение повернутого изображения
        output_path_270 = os.path.join(output_folder_270, file_name)
        rotated_image_270.save(output_path_270)
