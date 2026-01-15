# include<iostream>
# include<fstream>
#include <sstream>
# include<vector>
# include<string>
# include<iomanip>
# include<algorithm>
  using namespace std;
// TODO:  include needed files
struct Phone_Struct{
  string number;
  char phoneType;
};

// TODO: create Contact class per the document
class Contact{
   public:
      Contact(char contactType, string lastName, string firstName);
      Contact(char contactType, string number);
      Contact();
      bool operator<(const Contact& other);
      void  setEmail(string email){this->email = email;}
      void setFirstName(string firstName){this->firstName=firstName;};
      void setLastName(string lastName){this->lastName=lastName;};
      void setContactType(char contactType);
      void setDateOfBirth( string setdateOfBirth){this->dateOfBirth = setdateOfBirth;};
      string getEmail(){return email;}
      void setAddress(int streetNumber, string streetName, string city, string state, int postalCode){
         address = to_string(streetNumber) + " " + streetName + ", "+city+", "+state+" "+to_string(postalCode);}
      string tester();
      string getAddress()const{return address;}
      string getName()const{return lastName +", " + firstName;}
      string getFirstName()const{return firstName;};
      string getLastName()const{return lastName;};
      char getContactType()const{return contactType;};
      string getState()const{return state;};
      string getDateOfBirth()const{return dateOfBirth;};
      string addPhone(char phoneType, string number);
      string deletePhone (int index);
      string getAsString()const;
      

	private:
	   char contactType = 'e';
	   string  firstName = "empty";
	   string lastName = "empty";
	   string address = "empty";
	   string streetName = "empty";
	   string city = "empty";
     string state = "empty";
	   string email = "to be assigned";
	   string dateOfBirth = "empty";
	   int streetNumber = 0;
	   int postalCode = 0;
     vector<Phone_Struct> PhoneNumbers;
      string temp_num;
	   
};

class ContactList{
public:
  string loadContactsFromFile (string filename); 
  int getCount(){return contacts.size();};
  string sortContacts();
  vector<int> findContactsByName(string input);
  void printContacts();
  void printContacts(vector<int> input_vector);
  string addContact(Contact object);
  string deleteContact(int index);
  string tester();
  

private:
  vector<Contact> contacts;

};


// TODO: create the constructor (char, string, string)
Contact::Contact(){};
Contact::Contact(char contactType, string firstName, string lastName){
   this->contactType = contactType;
   this->firstName = firstName;
    this->lastName = lastName;};

Contact::Contact(char contactType, string number){
  this->contactType = contactType;
  temp_num = number;};

void Contact::setContactType(char contactType){
  this->contactType = contactType;
  cout << contactType;
}

string Contact::addPhone(char phoneType, string number){
  /*if(ContacType != 'W' || ContacType != 'H' || ContacType != 'C'){
  return "failure: invalid phone type - " + to_string(ContacType);}

  else{
    return "success: added number " + number + " " +  to_string(ContacType);}
    Phone_Struct Phone_temp;
    Phone_temp.number = number;
    Phone_temp.phoneType = ContacType;
    PhoneNumbers.push_back(Phone_temp);  */
  string type_output;
  if(phoneType == 'W' || phoneType == 'H' || phoneType == 'C'){
    if(phoneType == 'W'){
      type_output = " Work";}
    if(phoneType == 'H'){
      type_output = " Home";}
    if(phoneType == 'C'){
      type_output = " Cell";}
    Phone_Struct Phone_temp;
    Phone_temp.phoneType = phoneType;
    Phone_temp.number = number;
    PhoneNumbers.push_back(Phone_temp);
    return "success: added number " + number + type_output;}

  else{
    type_output.push_back(phoneType);
    return "failure: invalid phone type - " + type_output;
  }
  
}

string Contact::deletePhone (int index){

    if(index < int(PhoneNumbers.size()) && index >= 0){
      return "success: deleted phone " + to_string(index);
      PhoneNumbers.erase(PhoneNumbers.begin()+index);}
    else{
        return "failure: unable to delete phone " + to_string(index);}
  }

string Contact::getAsString()const{
   string output;
  string phone_temp;
  char phone_type;
  string sphone_type = "";
  string number;
  string contact_output;
  char temp_type = getContactType();
  
  if(contactType == 'W' || contactType == 'w'){
    contact_output = "Work";}

  
  if(temp_type == 'P'|| temp_type == 'p'){
    contact_output = "Personal";}

  
  for(int i = 0; i < int(PhoneNumbers.size()); i++){
    phone_type = (PhoneNumbers.at(i)).phoneType;
    if(phone_type == 'W'){
      sphone_type = "Work";}
    
    if(phone_type == 'H'){
      sphone_type = "Home";}
    
    if(phone_type == 'C'){
      sphone_type = "Cell";}

    number = (PhoneNumbers.at(i)).number;
    phone_temp += sphone_type + ": " + number + "\n";}
  
  output = lastName + ", " + firstName +"\n" + contact_output + "\n" + getAddress() + "\n" + getDateOfBirth() + "\n" + email + "\n" + phone_temp;
  return output;

  
  
  
  }


bool Contact::operator<(const Contact& other){
  return getName() < other.getName();}

// TODO: create the setEmail function

// TODO: create the getEmail function

// TODO: create the setAddress function

// TODO: create the getAddress function

// TODO: create the getName function



string ContactList::loadContactsFromFile(string filename){
  ifstream data(filename);
  

  vector<string> push_vector;
  
  if(data.is_open()){
    string text;
    getline(data, text);
    for(string line; getline(data, line);){
      stringstream stringstr(line);


      while (stringstr.good()){
        string substr;
        getline(stringstr, substr, ',');
        push_vector.push_back(substr);}//End while loop


      Contact loading_contact(toupper(push_vector.at(0).at(0)), push_vector.at(1),  push_vector.at(2));
      loading_contact.setAddress(stoi(push_vector.at(3)), push_vector.at(4), push_vector.at(5), push_vector.at(6), stoi(push_vector.at(7)));
      loading_contact.setEmail(push_vector.at(8));
      loading_contact.setDateOfBirth(push_vector.at(9));
      loading_contact.addPhone('H', push_vector.at(11));
      loading_contact.addPhone('C', push_vector.at(12));
      contacts.push_back(loading_contact);

      push_vector.clear();
    }//end for loop
    data.close();
    return "success: " + to_string(contacts.size()) + " added";
    }
    return "failure: " + filename + " not found";
  
  }//end fucntion

string ContactList::sortContacts(){
  sort(contacts.begin(), contacts.end());
  if(is_sorted(contacts.begin(), contacts.end())){
    return "success";
  }
  else{
    return "failure";
  }
}

vector<int> ContactList::findContactsByName(string input){
  vector<int> output_vector;
  Contact temp_contact;
  string temp_string;
  int index;
  transform(input.begin(), input.end(), input.begin(), ::toupper);
  for(int i = 0; i < int(contacts.size()); i++){
    temp_contact = contacts.at(i);
    temp_string = temp_contact.getName();
    transform(temp_string.begin(), temp_string.end(), temp_string.begin(), ::toupper);
    index = temp_string.find(input);
    if(index != -1){
      output_vector.push_back(i);
    }// end branch
    
  }// end for loop

  return output_vector;
}//end of function defintion


void ContactList::printContacts(){
  Contact tempC;
  for(int i = 0; i < int(contacts.size()); i++){
    tempC = contacts.at(i);
    cout << tempC.getAsString();
  }// end for loop


}// end function

void ContactList::printContacts(vector<int> input_vector){
  Contact tempC;
  for(int i = 0; i < int(input_vector.size()); i++){
    cout << "--------------------" << endl;
    cout << endl;
    tempC = contacts.at(input_vector.at(i));
    cout << tempC.getAsString() << endl;
  }// end loop
  
}// end function


string ContactList::addContact(Contact object){
  int old_size = int(contacts.size());
  contacts.push_back(object);
  if(int(contacts.size()) > old_size){
    return "success: " + object.getName() + " added";
  }// end branch
  
  else{
    return "failure: unable to add contact";
  }// end branch
}//end function

string ContactList::deleteContact(int index){
  string name;
  name = contacts.at(index).getName();
  int old_size = int(contacts.size());
  contacts.erase(contacts.begin() + index);
  if(int(contacts.size()) < old_size){
    return "success: deleted contact" + name;
  }// end of branchl
  else{
    return "failure: unable to delete contact " + to_string(index);
  }// end of branch
  
}
int main(){

  /*Contact c ('P', "Miles", "Davis");
   
   c.setEmail("miles.davis@uic.edu");
   
   cout << c.getEmail() << endl;    // miles.davis@uic.edu
   
   cout << c.getName() << endl;     // Davis, Miles
   
   c.setAddress(1200, "W. Harrison St", "Chicago", "IL", 60607); 
   
   cout << c.getAddress() << endl;     
   1200 W. Harrison St, Chicago, IL 60607*/

  ContactList List;
  List.loadContactsFromFile("contacts.csv");
  List.sortContacts();
  vector<int> test = List.findContactsByName("ra");
  
  List.printContacts(test);

  

  return 0;
}