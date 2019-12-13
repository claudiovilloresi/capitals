### Let's discover the European Capitals! 

In this repository you can find a file named ```main.py``` that, with a proper input, allow user to receive back the name of capitals and the respective state of Europe, and a file named ```dbmanager.py``` that requires you to insert a username and a password before doing anything else.

In order to run ```main.py``` you will need a username and a password. Therefore, the first step you have to do is to launch the file ```dbmanager.py``` and insert your *username* and a *password* by following two steps.

## 1. How to populate the database

To access ```main.py``` the user needs a username and a password that have to be previously added to the database. 
In order to *add* a specific user to the database you can use the ```dbmanager.py``` file, with the following parameters:

* -u: to add the username
* -p: to Set the password for the given username

In you want to *check* if your username and password have been successfully stored use the commands:

* -c
* -p

_Adding a user example_
```
python dbmanager.py -u ErPupone -p 10 -c Rome


```

_Checking a user example_
```
python dbmanager.py -c ErPupone -p 10 -c Rome


```

## 2. How to properly use the application

Once done the previous step, you can launch the file main.py, which will require some input as well.
In this case, the steps are the following:
-u = the user you added to the database
-p = your corresponding password
-c = to insert the capital
-s = to insert the state

Type this in the command line with the data you prefer (whatever capital or state permitted):
```
python main.py -u ErPupone -p 10 -c Rome

```

It will give you a result like this one:


If you find any trouble in doing these steps or if you need further info, please write ```-h``` or ```--help```. This command will give a hint on how to proceed.

## Data Files

The user can choose between a wide range of capitals or states of Europe and the they can be found in _.csv_ file located in: ```mypackage/list_of_capitals.csv```.

*Valid states and capitals:*

|State                 |Capital         |
|----------------------|----------------|
|Aland Islands         |Mariehamn       |
|Albania               |Tirana          |
|Andorra               |Andorra la Vella|
|Armenia               |Yerevan         |
|Austria               |Vienna          |
|Azerbaijan            |Baku            |
|Belarus               |Minsk           |
|Belgium               |Brussels        |
|Bosnia and Herzegovina|Sarajevo        |
|Bulgaria              |Sofia           |
|Croatia               |Zagreb          |
|Cyprus                |Nicosia         |
|Czech Republic        |Prague          |
|Denmark               |Copenhagen      |
|Estonia               |Tallinn         |
|Faroe Islands         |Torshavn        |
|Finland               |Helsinki        |
|France                |Paris           |
|Georgia               |Tbilisi         |
|Germany               |Berlin          |
|Gibraltar             |Gibraltar       |
|Greece                |Athens          |
|Guernsey              |Saint Peter Port|
|Hungary               |Budapest        |
|Iceland               |Reykjavik       |
|Ireland               |Dublin          |
|Isle of Man           |Douglas         |
|Italy                 |Rome            |
|Jersey                |Saint Helier    |
|Kosovo                |Pristina        |
|Latvia                |Riga            |
|Liechtenstein         |Vaduz           |
|Lithuania             |Vilnius         |
|Luxembourg            |Luxembourg      |
|Macedonia             |Skopje          |
|Malta                 |Valletta        |
|Moldova               |Chisinau        |
|Monaco                |Monaco          |
|Montenegro            |Podgorica       |
|Netherlands           |Amsterdam       |
|Northern Cyprus       |North Nicosia   |
|Norway                |Oslo            |
|Poland                |Warsaw          |
|Portugal              |Lisbon          |
|Romania               |Bucharest       |
|Russia                |Moscow          |
|San Marino            |San Marino      |
|Serbia                |Belgrade        |
|Slovakia              |Bratislava      |
|Slovenia              |Ljubljana       |
|Spain                 |Madrid          |
|Svalbard              |Longyearbyen    |
|Sweden                |Stockholm       |
|Switzerland           |Bern            |
|Turkey                |Ankara          |
|Ukraine               |Kyiv            |
|United Kingdom        |London          |
|Vatican City          |Vatican City    |

## Commands line parameters

Commands to use in *dbmanager.py*

* -h, --help: show the possible allowed arguments
* -u: give the possibility to add the username
* -p: Set the password for the given username
* -c: check if a username is present in the database

Commands to use in *main.py*

* -h, --help: shows the valid input for the two parameters
* -u: asks the user to input the username
* -p: asks for the correct password
* -c: give the possibility to choose a capital to discover the state
* -s: give the possibility to choose a state to discover its capital

## Testing

Tests on parts of the code are provided in the folder ```mypackages/tests/```, the module used to test ```main.py``` is ```test_main.py```.
Before you run the tests, you need to move inside capitals (so, ```cd capitals```) and then run: python3 -m unittest -v -b tests/test_main.py

```
python3 -m unittest -v -b tests/test_main.py
test_empty_datafie (tests.test_main.TestMain) ... ok
test_no_datafile (tests.test_main.TestMain) ... ok

----------------------------------------------------------------------
Ran 2 tests in 0.002s

OK
```

## Authors and Acknowledgement

Thank you all for using our application! Follow the authors on LinkedIn to be always up to date on following developments!

* [Bonacina Riccardo](www.linkedin.com/in/riccardo-bonacina-749735163/)
* [Callegaro Filippo](www.linkedin.com/in/filippocallegaro/)
* [Possagno Alberto](www.linkedin.com/in/albertopossagno)
* [Tomiazzo Matteo](www.linkedin.com/in/matteotomiazzo/)
* [Claudio Villoresi](www.linkedin.com/in/claudiovilloresi/)
