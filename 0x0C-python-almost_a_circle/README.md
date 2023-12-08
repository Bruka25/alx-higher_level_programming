The following python programs are for 0x0C-python-almost_a_circle project for the ALX higher level programming curriculum, inside it contains the following python functions:

* All the python files, classes and methods must be unit tested and be PEP 8 validated
* A folder named models with an empty file __init__.py inside - with this file, the folder will become a Python package
* Class Rectangle that inherits from Base
* Updated class Rectangle by adding validation of all setter methods and instantiation (id excluded)
* Updated class Rectangle by adding the public method def area(self): that returns the area value of the Rectangle instance
* Updated class Rectangle by adding the public method def display(self): that prints in stdout the Rectangle instance with the character # - you don’t need to handle x and y here
* Updated class Rectangle by overriding the __str__ method so that it returns [Rectangle] (<id>) <x>/<y> - <width>/<height>
* Updated class Rectangle by improving the public method def display(self): to print in stdout the Rectangle instance with the character # by taking care of x and y
* Updated class Rectangle by adding the public method def update(self, *args): that assigns an argument to each attribute
* Updated class Rectangle by updating the public method def update(self, *args): by changing the prototype to update(self, *args, **kwargs) that assigns a key/value argument to attributes
* Class Square that inherits from Rectangle
* Updated class Square by adding the public getter and setter size
* Updated class Square by adding the public method def update(self, *args, **kwargs) that assigns attributes
* Updated class Rectangle by adding the public method def to_dictionary(self): that returns the dictionary representation of a Rectangle
* Updated class Square by adding the public method def to_dictionary(self): that returns the dictionary representation of a Square
* Updated class Base by adding the static method def to_json_string(list_dictionaries): that returns the JSON string representation of list_dictionaries
* Updated class Base by adding the class method def save_to_file(cls, list_objs): that writes the JSON string representation of list_objs to a file
* Updated class Base by adding the static method def from_json_string(json_string): that returns the list of the JSON string representation json_string
* Updated class Base by adding the class method def create(cls, **dictionary): that returns an instance with all attributes already set
* Updated class Base by adding the class method def load_from_file(cls): that returns a list of instances
* Updated class Base by adding the class methods def save_to_file_csv(cls, list_objs): and def load_from_file_csv(cls): that serializes and deserializes in CSV
* Updated class Base by adding the static method def draw(list_rectangles, list_squares): that opens a window and draws all the Rectangles and Squares
