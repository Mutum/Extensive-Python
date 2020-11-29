# Epai_Session_5_test


## Time It Function
Write a function which gives out average run time per call, such that it's definition is:

def time_it(fn, *args, repetitons= 1, **kwargs): your code comes here.

We should be able to call it like this:

- time_it(print, 1, 2, 3, sep='-', end= ' ***\n'. repetitons=5)
- time_it(squared_power_list, 2, start=0, end=5, repetitons=5) #2 is the number you are calculating power of, [1, 2, 4, 8, 16, 32]
- time_it(polygon_area, 15, sides = 3, repetitons=10) # 15 is the side length. This polygon supports area calculations of upto a hexagon
- time_it(temp_converter, 100, temp_given_in = 'f', repetitons=100) # 100 is the base temperature given to be converted
- time_it(speed_converter, 100, dist='km', time='min', repetitons=200) #dist can be km/m/ft/yrd, time can be ms/s/m/hr/day, speed given by user is in kmph

### Functions definition

#### 1. time_it
This functions calls any define or inbuilt python functions and runs the functions per certain repetitions and return the average run time per call.
The functions is a use case of *args and **kwargs .
Going drill down on the functions " def time_it(fn, *args, repetitons= 1, **kwargs) " , here
 - fn : this is any arbitrary functions to be call repetively inside time_it function to give average run time per fn call
 - *args : This scoops up any arbitrary position arguments of the Functions
 - **kwargs : Same case as *args yet this will scoops up any arbitrary key-word arguments of the Functions. The **kwargs makes a dictionary of the input key-word arguments and finally unpack while calling time_it function
 - repetitons : this is decide the number of times the arbitrary function "fn" to be call inside time_it function . The default is set to 1 repetitons

#### 2. squared_power_list
This function allows for any arbitrary integer (greater than zero), we can calculate the power of the integer
The range for the go for the power is define by the key-word arguments "start"  and "stop" where their default are set to 0 and 5 respectively
Functions representation  is squared_power_list(a, *, start=0, end=5) where the * indicate the exhaustion of positional arguments, in other words the functions force user to atleast key one postinal arguments "a"

#### 3. polygon_area
The area calculation is restricted to polygon of :
 - triangle
 - square
 - rectangle
 - pentagon
 - Regular hexagon
 Any inputs of side not within the range of 3-6 inclusive will not work.

#### 4. temp_converter
Temperature conversion into farenhiet or celcuis vice versa
Again the * in function representation makes user to force one positional arguments

#### 5. speed_converter
For any user inputs of kmph ( kilometers per hours), the functions convert to given arbitrary units.
Units support in this functions are:
 - distance : kilometers, metres, feet, yard
 - time : hour, minutes, seconds, milliseconds, day
