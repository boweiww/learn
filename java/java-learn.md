1. A 'hello world' in java:
public class MyClass {
  public static void main(String[] args) {
    System.out.println("Hello World");
  }
}<br />

2.Java is an object oriented language which gives a clear structure to programs and allows code to be reused, lowering development costs. As Java is close to C++ and C#, it makes it easy for programmers to switch to Java or vice versa.<br />

3.Compile Java C:\Users\Your Name>javac MyClass.java. Run compiled file: C:\Users\Your Name>java MyClass. Remember that you need to make sure there is javac.exe exist in you java/bin folder. <br />

4.A class should always start with an uppercase first letter. Java is case-sensitive: "MyClass" and "myclass" has different meaning.<br />

5.The name of the java file must match the class name and that every program must contain the main() method.<br />

6.Syntex for declearing Java variable: type variable = value;<br />

7.However, you can add the final keyword if you don't want others (or yourself) to overwrite existing values (this will declare the variable as "final" or "constant", which means unchangeable and read-only)<br />

8.Primitive data types - includes byte, short, int, long, float, double, boolean and char Non-primitive data types - such as String, Arrays and Classes <br />

9.The long data type should end the value with an "L". The float data type should end the value with an "f". The double data type should end the value with a "d".
<br />
10.The precision of float is only six or seven decimal digits, while double variables have a precision of about 15 digits. Therefore it is safer to use double for most calculations.<br />

11.Alternatively, you can use ASCII values to display certain characters: char a = 65, b = 66, c = 67;<br />

12.Widening Casting (automatically) - converting a smaller type to a larger type size: byte -> short -> char -> int -> long -> float -> double<br />

13.Narrowing casting: double myDouble = 9.78; int myInt = (int) myDouble;   (myInt = 9)<br />

14.Find the postion of a character in string: String txt = "Please locate where 'locate' occurs!"; System.out.println(txt.indexOf("locate")); // Outputs 7<br />

15.  .concat() is similar to "string" + " " + "string"<br />

16.If need to write quote double quote or slash in a string, you need to add a slash before them: String txt = "We are the so-called \"Vikings\" from the north.";
<br />
17.The Math.sqrt(x) method returns the square root of x.<br />

18.Math.random() returns a random number between 0.0 (inclusive), and 1.0 (exclusive): 
  int randomNum = (int)(Math.random() * 101);  // 0 to 100<br />

19.Ternary Operator： variable = (condition) ? expressionTrue :  expressionFalse;<br />

20.Switch in Java: 
The switch expression is evaluated once.
The value of the expression is compared with the values of each case.
If there is a match, the associated block of code is executed.
The default keyword specifies some code to run if there is no case match.
The break and default keywords are optional, and will be described later in this chapter
<br />

21.for each loop in Java:
for (type variableName : arrayName) {....}<br />

22.To declare an array, define the variable type with square brackets: 
String[] cars;  int[] myNum = {10, 20, 30, 40};<br />

23.To find out how many elements an array has, use the length property:<br />

24.To create a two-dimensional array, add each array within its own set of curly braces:
int[][] myNumbers = { {1, 2, 3, 4}, {5, 6, 7} };<br />

25.A method is a block of code which only runs when it is called.You can pass data, known as parameters, into a method. Methods are used to perform certain actions, and they are also known as functions. Why use methods? To reuse code: define the code once, and use it many times.<br />

26.When a parameter is passed to the method, it is called an argument. So, from the example above: fname is a parameter, while Liam, Jenny and Anja are arguments.
<br />
27.With method overloading, multiple methods can have the same name with different parameters:
int myMethod(int x)
float myMethod(float x)
double myMethod(double x, double y)<br />

28.











