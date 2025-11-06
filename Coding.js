// Modify Array data 
var ourArray = [18,64,99];
ourArray[1] = 45;
//console.log(ourArray);

//Access Multi dimensional array
var myArray = [[1,2,3],[4,5,6],[[7,8,9],10,11]]
var myData = myArray[2][0][0]
//console.log(myData);

//Push function (add)
var ourArray =["Stimpson","J","cat"];
ourArray.push(["happy","joy"]);
//console.log(ourArray);

// Pop function (remove the last value)
var ourArray = [1,2,3];
var removeFromOurArray = ourArray.pop(); // remove the last value
//console.log(removeFromOurArray);

//Shift function (remove the first value)
var ourArray =["Stimpson","J","cat"];
var removeFromOurArray = ourArray.shift();
//console.log(removeFromOurArray);

//Unshift function (same as push but add value to the beginning of the array)
var ourArray =["Stimpson","J","cat"];
ourArray.shift();
ourArray.unshift("Happy");
//console.log(ourArray);

//Shopping list 
var myList = [["cereal", 3],["milk",2],["banana",3],["juice",2],["eggs",12]];

//Function allows us to reusable code 
function ourReusableFunction() {
    console.log("Heyya, World");
}
//ourReusableFunction();

//Argument 
function ourFunctionWithArgs(a,b){
    console.log(a-b);
}
//ourFunctionWithArgs(10,5);

//Global scope 
var myGlobal = 10;
function fun1(){
    oopsGlobal = 5; // if no var, it becomes global variable
}

function fun2(){
    var output ="";
    if (typeof myGlobal != "undefined"){
        output += "myGlobal: "+ myGlobal;
    }
    if (typeof oopsGlobal != "undefined"){
        output += "\noopsGlobal: " + oopsGlobal;
    }
    console.log(output);
}
//fun1();
//fun2();


//Local Scope
function myLocalScope(){
    var myVar =5;
    console.log(myVar);
}
//myLocalScope();
//0console.log(myVar); // Error 

//Global VS Local 
var outerWear = "T-Shirt";
function myOutfit(){
    var outerWear = "sweater";
    return outerWear;
}

//console.log(myOutfit());
//console.log(outerWear);

var sum = 0;
function addFive(){
    sum += 5;
}
//addFive(); // nothing happen 
//console.log(sum); // sum is 5

//Assign return variable 
var changed = 0;

function change(num){
    return (num+5)/3;
}
changed = change(10);

//Stand in line
function nextInLine(arr,item){
    arr.push(item)
    return arr.shift();
}
var testArr =[1,2,3,4,5,6];
// console.log("Before: " +JSON.stringify(testArr));
// console.log(nextInLine(testArr, 6));
// console.log("After: " +JSON.stringify(testArr));


//Boolean 
function welcomeToBoolean(){
    return false;
}

//If statement 
function ourTrueOrFalse(isItTrue){
    if(isItTrue){
        return "Yes, it's true";
    }
    return "No, it's false";
}
//console.log(ourTrueOrFalse(true));


//Equality operator
function testEqual(val){
    if(val == 12){
        return "Equal";
    }
    return "Not equal";
}
// console.log(testEqual(10));

function testStrict(val){
    if(val === 3){   // === not convert the type of value 
        return "Equal";
    }
    return "Not Equal";
}
// testStrict(3);//true
// testStrict("3");//false

// Inequality operator 
function testNotEqual(val){
    if (val != 99){ //strict would be !==
        return "Not Equal";
    }
    return "Equal"
}

// AND OR 
function testLogicalAnd(val){
    if (val <= 50 && val >= 25){
        return "Yes"; //
    }
    return "No";
}
function testLogicalOr(val){
    if (val < 10 || val > 20){
        return "Yes"; //
    }
    return "No";
}

// ELse 
function testElse(val){
    var result = "";
    if ( val > 5){
        result ="Bigger than 5";
    } else {
        result = "5 or Smaller";
    }
    return result;
}


// Else If
function testElseIf(val){
    if (val > 10) {
        return "Greater than 10";
    } else if (val < 5){
        return "Smaller than 5";
    } else {
        return "Between 5 and 10";
    }
}

// Chaining If-Else statement 

function testSize(num){
    if(num < 5){
        return "Tiny";
    } else if (num <10){
        return "Small";
    } else if (num < 15){
        return "Medium";
    } else if (num < 20) {
        return "Large";
    } else {
        return "Huge";
    }
}
//console.log(testSize(21));

//Switch Statement 
function caseInSwitch(val){
    var answer = "";
    switch(val){
        case 1: 
            answer = "alpha";
            break;
        case 2:
            answer = "beta";
            break;
        case 3: 
            answer = "gamma";
            break;

    }
    return answer;
}
 //console.log(caseInSwitch(1));

 //Running Boolean Values from function 
 function isLess(a,b){
    return a < b; // This's gonna be true/false result 
 }

 //Return Early Pattern for Functions
 function abTest(a,b){
    if (a < 0 || b < 0){
        return undefined;
    }
    return Math.round(Math.pow(Math.sqrt(a)+Math.sqrt(b),2));
 }

 //Build Object  // same as Array but use property to access value 
 var ourDog = {
    "name" : "Camper",
    "legs" : 4,
    "tails" : 1,
    "friends" : ["everything"]
 };

 // Dot Notation // Access property 
 var nameValue = ourDog.name;
 var legValue = ourDog.legs;
//  console.log(nameValue);
//  console.log(legValue);

//Bracket Notation 
var testObj ={ 
    "an entree":"hamburger",
    "my side": "veggie",
    "the drink" : "water"
};
var entreeValue = testObj['an entree'];
var drinkValue = testObj['the drink'];

// Accessing Object property via variable 
var testObj ={
    16 : "Montana"
};
var playerNumeber = 16;
var player = testObj[playerNumeber]
// console.log(player);

// Updatimg Object properties
 var ourDog = {
    "name" : "Camper",
    "legs" : 4,
    "tails" : 1,
    "friends" : ["everything"]
 };
ourDog.name = "Happy Camper";
// console.log(ourDog.name);

// Adding new property 
ourDog.bark = "bah bah";
// console.log(ourDog.bark);

//Delete property
delete ourDog.bark;


//Using Object for lookups
var lookup  = {
    "alpha" : "Adams",
    "bravo" : "Boston"
}


// Testing Obj property 

var myObj = {
    gift: "pony",
    pet : "kitten"
}

function checkObj(checkProp){
    if (myObj.hasOwnProperty(checkProp)){
        return myObj[checkProp];
    } else {
        return " Not found"
    }
}
// console.log(checkObj('gift')); 

// Manipulating Complex  Objects 
// Array of Objects 
var myMusic = [
    {
        "artist": "Billy Joel",
        "title": "Piano Man",
        "release_year": 1973,
        "format":[
            "CD",
            "8T",
            "LP"
        ],
        "gold":true
    },
    {
        "artist": "Beau Carnes",
        "title": "Cereal Man",
        "release_year": 2003,
        "format":[
            "Youtube video",
            "8T",
            "LP"
        ]
    }
]
