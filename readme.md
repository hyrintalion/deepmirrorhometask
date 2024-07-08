## Task:

Design and implement a system 
* that applies a non-deterministic function to a column (m) of a dataset containing n x m values (n is rows and m is columns), 
* ensuring real-time updates are visible. 
* The system should allow users to view the dataset in real time 
* and request updates (i.e. apply the fucntion). 
* Given 
    * that the function's execution time varies between 10ms to 300ms (per input) 
    * and the dataset could have up to 50k rows and 10 columns, 
* outline a simplified and testable approach.

## Guidelines:

    Set aside 3 hours. We understand that a fully tested solution for this problem would be very challenging to accomplish within three hours and that there would be multiple solutions with varying complexities. Therefore, we encourage you to build a simple prototype that can be extended. 

    Use your preferred programming language (such as Python, Java, or Go) and ensure that tests are included with your solution to demonstrate quality and correctness. The solution should also include unit tests for key functionalities. 

    Once finished, zip the code and email it to ryan@deepmirror.ai. Include instructions for running the code. We will assess your ability to design and test a flexible system that can be extended. 

## Example Pseudo-code:

// Component 1: Real-time Dataset Management and Notification

Initialize Loop

dataset = Reference or Initialize Dataset()

If there is an update_event:

dataset = Get updated Dataset()

Notify users with the new dataset

Else:

Sleep for a short period before checking for updates again

End Loop


// Component 2: Function Execution and Update Triggering

Function OperateAndUpdate(input):

Apply function to the input

Trigger an update event

End Function 

## Questions


    1. I have an assumption that the user - it is  the person who is calling this function. Is that right? Should I think about how many users could call a function? 

 

For a single dataset it could be a few users i.e. 10 calling it in the most complex case.

 

    2. How is the dataset updated - by some third party? Does it happen asynchronously somewhere else and I don't need to think about it too much?

 

Don’t think about it too much.

 

    3. Do you need some console app or should I create a tiny-tiny html for it?

 

Running in the terminal is fine i.e. while loop with print statement or to console.


    4. That function should contain? Some kind of random change of the data from the dataset? What changes should be made to a data that makes a function non-deterministic?

Use that if you call func(x1) -> y1 and if you were to evaluate again func(x1) -> y2. Doesn’t really matter as long as it’s not the same each time you call func 😊