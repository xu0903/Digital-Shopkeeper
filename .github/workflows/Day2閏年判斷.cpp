#include <iostream>
using namespace std;

int main()

{
int year = 0 ,month = 0;
cout << "Choose one year typing in number,pls.\n";
cin >> year;
cout << "Choose one one month typing in number,pls.\n";
cin >> month;
int days = 0;

switch(month)
	{
	 case 1: case 3: case 5: case 7: case 8: case 10: case 12:
	 days = 31;
	 break;
	 case 4: case 6: case 9: case 11:
	 days = 30 ;
	 break;
	 case 2:
		if ((year % 4 == 0 && year % 100 != 0 ) || year % 400 == 0  )
	    days = 29;
	    else
	    days =28;
	 default:
	    cout << "Pls type a correct number of month again.\n";
	}   
	switch(month)
	 {
	 case 1:
		cout << "There are "<< days << " days in " << month << "st month."<<"\n";
	  break;
	 case 2:
		cout << "There are "<< days << " days in " << month << "nd month."<<"\n";
	  break;
	 case 3:
		cout << "There are "<< days << " days in " << month << "rd month."<<"\n";
	  break;
    default:
	    cout << "There are "<< days << " days in " << month << "th month."<<"\n";
     break;
	 
	}

int sum = 0;
int i = 1;

while(i <= 10)
 { 
 cout << i <<"\n";
 sum = i++;
 }

 return 0;

	return 0;
} 







