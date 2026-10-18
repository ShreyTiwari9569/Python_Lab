from PIL import Image, ImageFilter

# Open an image
filename = input("Enter image filename (e.g., photo.jpg): ")

try:
    image = Image.open(filename)
    image = image.convert("RGB")

    print("\nChoose Image Operation:")
    print("1. Grayscale")
    print("2. Black and White (Threshold)")
    print("3. Blur")
    print("4. Display Image Information")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        # Convert image to grayscale
        result = image.convert("L")
        print("Image converted to grayscale.")

    elif choice == 2:
        # Convert to grayscale and apply threshold
        gray = image.convert("L")
        threshold = int(input("Enter threshold (0-255): "))

        result = gray.point(
            lambda pixel: 255 if pixel >= threshold else 0
        )
        print("Black and white image generated.")

    elif choice == 3:
        # Apply blur filter
        result = image.filter(ImageFilter.BLUR)
        print("Blur filter applied.")

    elif choice == 4:
        # Display image information
        print("Image Format:", Image.open(filename).format)
        print("Image Size:", image.size)
        print("Color Mode:", image.mode)
        result = image

    else:
        print("Invalid choice.")
        result = None

    if result is not None:
        if choice != 4:
            output_file = input(
                "Enter output filename (e.g., output.png): "
            )
            result.save(output_file)
            print("Processed image saved as", output_file)

        result.show()

except FileNotFoundError:
    print("Error: Image file not found.")

except OSError:
    print("Error: Unable to open the image.")

except ValueError:
    print("Error: Please enter a valid number.")