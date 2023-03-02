# IO Method Handler  

## Problem
The problem occurs when a method has an io call - such as taking input from a user - and it needs to be invoked multiple
times with different inputs automatically. It becomes very useful in terms of
method analysis such as camping multiple methods. Sometimes it is needed to 
trigger the time or the number of invocations.\
The script uses builtin libs, no external packages are needed to be installed 

## How to use it?
Assuming we have the following method:
```python
def multiply():
    num1, num2 = map(int, input().split())
    num3, num4 = map(int, input().split())
    return num1 * num2 * num3 * num4
```
It takes two inputs from a user, each one has two numbers separated by space, for example:
```shell
1 2
3 4
```
Use the handler to deal with io calls 
```python
from handler import IOHandler

func = IOHandler(multiply)
print(func('5 6\n2 1'))
```
```shell
 60
```
Somtimes, it needs to trigger the number of calling 
```python
from handler import CountedIOHandler

func = CountedIOHandler(multiply)
for _ in range(10):
    func('5 6\n2 1')

print(func.counter)
```
```shell
10
```
In other cases, it needs to calculate the time of calling 
```python
from handler import TimedIOHandler

func = TimedIOHandler(multiply)
func('5 6\n2 1')

print(func.start_time)
print(func.end_time)
print(func.total_time)
```
To use the capability of both counter  rand timer 
```python
from handler import TimedCountedIOHandler

func = TimedCountedIOHandler(multiply)
func('5 6\n2 1')

print(func.start_time)
print(func.end_time)
print(func.total_time)
print(func.counter)
```
It is not limited to String IO, also **File** could be used
```python
import io
from handler import IOHandler

func = IOHandler(multiply, io.FileIO)
func('file.txt')
```
**Note** that the file should follow the previously shown format 