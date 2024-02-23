#If class exist then add to it don't overwrite it
    #But still replace the same class with the new style
#If class does not exist append to the CSS file don't remove everything

#Account for more than one class or style to change
#Check to see if way to use these files to take input on webpage and change the css file
def change_css():
    css_class = '.todo li' #input("Enter the CSS class to change: ")
    css_style = input("Enter the new CSS style: IE: color:blue ")

    #Read the file to ensure we can utilize the user input if it is valid/exist within the css document tochange it
    with open('style.css', 'r') as file:
        css_file = file.read()

    #Check if user class input exist in css file. If so replace old class with the new class
    if css_class in css_file:
        css_file = css_file.replace(f"{css_class} {{}}", "")
        new_css_file = f"{css_class} {{\n   {css_style}\n}}"

    else:
        print("The class you entered is nonexistent...creating it for you now! \n YOU'RE WELCOME!")

        new_css_file = f"{css_class} {{\n   {css_style}\n}}"

    #Now write the changes to the file
    with open('style.css', 'w') as file:
        file.write(new_css_file)

change_css()
