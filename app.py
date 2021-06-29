import pdfkit

option = input("Please select if file is local (L) or web (W): ")

if option == 'L':
    the_file = input("Enter the file fullname: ")
    pdfkit.from_file(the_file, 'output_file.pdf')
elif option == 'W':
    the_url = input("Enter the full url: ")
    pdfkit.from_url(the_url,'output_url.pdf')
else:
    TypeError

print("File has been created at app directory")
