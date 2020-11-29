# EPAI Session 2

## Something
A class that assigns an attribute called something_new and initializes with None. 

## SomethingNew
A class that takes an interger along with something object as input. Both the input parameters i and something are initialized with 0 and None respectively. It assigns the input parameter something as a varible to itself

## add_something
A funtion which takes collection and i as input parameters .It then instantiates objects for each of the classes Something and SomethingNew and set SomethingNew class object as a variable to the Something instance object followed by appending the latter to the collection list parameter.

## clear_memory
A function that take a  list as parameter and delets them

## critical_function
function that initializes collection as a list. It runs a loop to call add_something 131071 times . Once loop is finished, it calls clear_memory to delete the created class objets and their object`s memory

## compare_strings_old
function that assigns a very long string to two variables a and b. It runs a loop equal to the n times that is input parameter to the function. In that loop it does string comparison between a between b using == syntax that actually does the comparison character by character. The function also creates a list of all the characters in the string and run a loop for n times to check if the character 'd' is present in the list. This function actually runs slow because of the following reasons: Since the string is quite long and does not follow any peephole standard, python stores the objects of a and b variables in two different memory locations although the string value is same. Using == actually compares character by character Checking presence of an elements in a list or tuple is much slower compared to hashed membership

## compare_strings_new
Function that does the similar job as compare_strings_old however in more efficient and optimized way. 
It assigns the same long sting to two variables a and b. However, it forcefully interns the string so that python remembers the memory location and does not store that in a new memory location everytime it is called. 
For the comparison it uses if a is b that actually checks if the memory location of a is same as that of b which in fact is the case. Hence this step is quite faster. Moreover the function creates a set of all the characters of the string to check if 'd' is present in that n time in a loop. Since the set is hashed, it runs pretty fast.

## sleep
function of time class that was deliberately put in in case of compare_strings_new so that we delete that and rewrite optimized compare_strings_new function. Sleep takes argument of number of seconds when called and pauses the programs execution for the specified amount of time.

## char_list
Is created when list function was applied to the long string. Every character in the string is separated as separate element and stored in the list char_list. It does follow the order however with inclusion of duplicates.

## collection
A list of all the class objects of Something class created when critical_function got executed.

## __init__
Python reserved method of a class. It is used to initialize the attributes of a class.
