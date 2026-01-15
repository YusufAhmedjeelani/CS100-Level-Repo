#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <algorithm>
#include <cctype>
#include "stdlib.h"

#include "Contact.h"
#include "ContactList.h"

using namespace std;
void printMainMenu(){
  cout << "********************************************" << endl;
  cout << "Main Menu" << endl;
  cout << endl << "Enter the letter for the desired menu option:" << endl;
  cout << "   C - Get count" << endl;
  cout << "   L - Load contacts from file" << endl;
  cout << "   S - Search contacts" << endl;
  cout << "   P - Print contacts" << endl;
  cout << "   X - Exit" << endl;
}//Void function to print out menu options
void printReplyMenu(){
cout << "Enter an option:" << endl;
cout << "   P - Print contacts" << endl;
cout << "   or a Contact number to view/edit" << endl;
cout << "   R - Return to main menu" << endl;
}//Void function to print out Reply Menu options

void Personchoice(){
cout << "Enter an option for contact:" << endl;
cout << "   A - Edit address" << endl;
cout << "   B - Edit date of birth" << endl;
cout << "   E - Edit email address" << endl;
cout << "   N - Edit name" << endl;
cout << "   P - Edit phone numbers" << endl;
cout << "   R - Return to main menu" << endl;
cout << "   D - Delete" << endl;
}//Void function to print out options for a contact

void PhoneOptions(){
cout << "Enter an option:" << endl;
cout << "   A - Add a phone number" << endl;
cout << "   R - Return to main menu" << endl;
cout << "   or list number to delete" << endl;
}//Void function to print out 
int main(){
  string result;
ContactList List;
//result = List.loadContactsFromFile("contacts.csv");
vector<int> posVector; 
char reply;
  printMainMenu();
  cin >> reply;
  reply = toupper(reply);
  while(reply != 'X'){
    
    if (reply == 'C'){
      //FINISH ME
      int count;
      count = List.getCount();
      cout << "There are " + to_string(count) + " contacts" << endl << endl;
      
    }//end main C branch
     else if (reply == 'L'){
      //FINISH ME
       string fileName;
       cout << "Enter a filename" << endl;
       cin >> fileName;
       result = List.loadContactsFromFile(fileName);
       cout << result << endl << endl;
    }//end main L branch
     else if (reply == 'S'){
      //FINISH ME
       string searchT;
       string tempO;
       char option;
       cout << "Enter a search term" << endl;
       cin >> searchT;
       posVector = List.findContactsByName(searchT);
       if(posVector.size() != 1){
       cout << endl << "Found " + to_string(posVector.size()) + " results" << endl;}

       else{
          cout << endl << "Found " + to_string(posVector.size()) + " result" << endl;}
       //List.printContacts(posVector);
       for(int i = 0; i < posVector.size(); i++){
         cout << to_string(i+1)+"." << " ";
         cout << List.getContact(posVector.at(i))->getLastName() << ", " << List.getContact(posVector.at(i))->getFirstName() << endl;}//END for loop
        printReplyMenu();
        cin >> tempO;
       option = tempO.at(0);
        option = toupper(option);
       while(option != 'R' || option != 'X'){
         if (option == 'P'){
             List.printContacts(posVector);
              break;}//End Print all contacts with search term
         else if(isdigit(option)){
            int num = option - 48;
            int newNum = stoi(tempO);
            cout << List.getContact(posVector.at((newNum)-1))->getAsString();
            Personchoice();
            char Personresponse;
            string Changeinfo;
            cin >> Personresponse;
            Personresponse = toupper(Personresponse);
            if(Personresponse == 'E'){
                cout << "Current email:" << endl;
                cout << List.getContact(posVector.at((num)-1))->getEmail() << endl << endl;
                cout << "Enter new email or C to cancel:" << endl;
                cin >> Changeinfo;
                if(Changeinfo != "C" && Changeinfo != "c"){
                  List.getContact(posVector.at((num)-1))->setEmail(Changeinfo);
                  cout << endl << "Email updated:" << endl;
                  cout << Changeinfo << endl;      
                  break;}// personresponsebranch
                else{
                  break;}//Handles cancels
              }//end of E
            if(Personresponse == 'P'){
              char PhoneResponse;
              char PhoneType;
              string phoneType;
              string Number;
              vector<string> phone_list = List.getContact(posVector.at((num)-1))->getPhoneNumbers();
              if(phone_list.size() != 1){
              cout << "Found " << phone_list.size() << " phone numbers"<<endl;}
              else{
                cout << "Found " << phone_list.size() << " phone number"<<endl;}
              for(int i =0; i < phone_list.size(); i++){
                cout << i+1 << ". " << phone_list.at(i) << endl;
                }//end loops that outputs phone#s
                PhoneOptions();
                cin>>PhoneResponse;
                while(PhoneResponse != 'R' || PhoneResponse != 'r'){
                  if(PhoneResponse == 'A' || PhoneResponse == 'a'){
                    cout << "Enter the letter for the phone number type:" << endl << "C(ell), W(ork) or H(ome)" << endl;
                    cin >> PhoneType;
                    if(PhoneType == 'C'){
                      phoneType = "Cell";}
                    else if(PhoneType == 'W'){
                      phoneType = "Work";}
                    else if(PhoneType == 'H'){
                      phoneType = "Home";}
                    cout << "Enter the phone number:" << endl;
                    cin >> Number;
                    List.getContact(posVector.at((num)-1))->addPhone(PhoneType, Number);
                    cout << "success: added number " << Number + " " + phoneType << endl;
                    break;
                  }//End add # branch
                 else if(isdigit(PhoneResponse)){
                      int num2 = PhoneResponse - 48;
                      char delResponse;
                      string outputN;
                      for(int i = 0; i <  phone_list.at(num2-1).size(); i++){
                        if(isdigit(phone_list.at(num2-1).at(i))||phone_list.at(num2-1).at(i) == 'C' || phone_list.at(num2-1).at(i) == ')' || phone_list.at(num2-1).at(i) == '-'|| phone_list.at(num2-1).at(i) == '('|| phone_list.at(num2-1).at(i) == ' '){
                          outputN.push_back(phone_list.at(num2-1).at(i));}//end branch
                      }//end loop to get only # from string
                      cout << "Are you sure you want to delete phone:  " << phone_list.at(num2-1) + "?" << endl;
                      cout << "Enter 'Y' to confirm." << endl;
                      cin >> delResponse;
                      if(delResponse == 'Y' || delResponse == 'y'){
                        cout << "success: deleted phone " <<  outputN << endl;
                        List.getContact(posVector.at((num)-1))->deletePhone(num2-1);
                      
                        break;}// Conformation branch
                      break;}// ends branch that deletes number
                else{
                  break;
                }     
                }// Ends while loop
            
    
            }//end of P
            if(Personresponse == 'D'){
              string deleteResp;
              cout << "Are you sure you want to delete contact " << List.getContact(posVector.at((num)-1))->getName() + "?" << endl;
              cout << "Enter 'Y' to confirm." << endl;
              cin >> deleteResp;
              if(deleteResp =="Y" ||deleteResp =="y"){
                cout << "success: deleted contact " << List.getContact(posVector.at((num)-1))->getName() << endl;
                List.deleteContact(posVector.at((num)-1));
                break;}//Confirmes and deletes contact
            }//DELETES CONTACT
         }//End working with single contact
         break;
       }// end while loop 
    }//End main S branch     
     else if (reply == 'P'){
      //FINISH ME
      //vector<int> FullList;
       /*for(int i =0; i < count; i++){
         FullList.push_back(i);}*/
      List.printContacts();
       //cout << "Branch used" << endl;
    }// end main P branch  
    else{
      cout << "Invalid Input:" << endl;
    }// else branch
  cout << endl;
  printMainMenu();
    cin >> reply;
    reply = toupper(reply);   
  }
  return 0;
}