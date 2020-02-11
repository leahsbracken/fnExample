# fnExample Instructions
A simple example using Functions 

### Create a new directory of where you want to put the project 
mkdir fn examples

### Create a new file 

fn init --runtime python moviePython

### cd into the directory

cd moviePython

### Create an app

fn create app movieApp

### Deploy the applications

fn --verbose deploy --app movieApp --local

### Invoke the function 

fn invoke movieApp moviePython

### From the fn invoke, should see the following output:

{"movie": "Thor", "director": "Kenneth Branagh"}

### You can also pass data to the incoke command; try passing "Iron Man," or "Spider-Man: Homecoming"

echo -n '{"movie":"Iron Man"}' | fn invoke movieApp moviePtyhon --content-type application/json

### To call the function by URL, use the Fn invoke command to find the endpoint

fn inspect function movieApp moviePython



