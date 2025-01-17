# Let's discover the European Capitals!

In this repository you can find a file named ```main.py``` that, with a proper input, allows the user to enter a country or capital and receive, in return, the corresponding European capital or country.

You can find also a file named ```dbmanager.py``` that requires you to insert a username and a password before doing anything else.

In order to run ```main.py``` you will need a username and a password. Therefore, the first step you have to do is to launch the file ```dbmanager.py``` and insert your *username* and a *password* by following two steps.

## 1. How to populate the database

To access ```main.py``` the user needs a username and a password that have to be previously added to the database.
In order to *add* a specific user to the database you can use the ```dbmanager.py``` file, with the following parameters:

* -u: to add the username
* -p: to Set the password for the given username

_Adding a user example_
```
python dbmanager.py -u Mario -p 10
```

## 2. How to properly use the application

Once done the previous step, you can launch the file ```main.py```, which will require some input as well.
In this case, the steps are the following:
* -user = the user you added to the database
* -p = your corresponding password

AND
* -c = to insert the capital
<br>OR
* -s = to insert the state

You have to type either -c or -s, not both of them (indeed, you can select either a capital or a state).

Type this in the command line with the data you prefer (whatever capital or state permitted):
```
python main.py -user Mario -p 10 -c Rome
```

It will give you a result like this one, if you are allowed to run the code:
```
User is present, password is valid
The European state whose capital is Rome is Italy
```
Otherwise:
```
Username does not exist or password is incorrect
```

If you find any trouble in doing these steps or if you need further info, please write ```-h``` or ```--help```. This command will give a hint on how to proceed.

## Data Files

The user can choose between a wide range of capitals or states of Europe and they can be found in _.csv_ file located in: ```mypackage/list_of_capitals.csv```.

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

Commands to use in *main.py*

* -h, --help: shows the valid input for the two parameters
* -user: asks the user to input the username
* -p: asks for the correct password
* -c: give the possibility to choose a capital to discover the state
* -s: give the possibility to choose a state to discover its capital

## Testing

Tests on parts of the code are provided in the folder ```mypackages/tests/```, the module used to test ```main.py``` is ```test_main.py```.
The command line to run the tests is: ```python3 -m unittest -v -b tests/test_main.py```
N.B. In order to properly run the code, use ```python3```
```
python3 -m unittest -v -b tests/test_main.py
test_empty_datafie (tests.test_main.TestMain) ... ok
test_no_datafile (tests.test_main.TestMain) ... ok

----------------------------------------------------------------------
Ran 2 tests in 0.002s

OK
```

## PEP-8

All the python modules used to run and create the application follow the PEP-8 guidelines and set of rules.

## Authors and Acknowledgement

Thank you all for using our application!

* Bonacina Riccardo
* Callegaro Filippo
* Possagno Alberto
* Tomiazzo Matteo
* Villoresi Claudio

## License

MIT License
