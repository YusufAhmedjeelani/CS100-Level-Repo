
//Program 6
//CS141 Spring 23
//Professor David Hayes
//Author: Yusuf Ahmedjeelani
//Given an input file, create an Adjancy List, export it to a file and output data of the list
#include <iostream>
#include <vector>
#include <string>
#include <iomanip>
#include <sstream>
#include <fstream>
#include <random>
#include <algorithm>

using namespace std;

class Nodeoflinkedlist{
  public:
  int ID;
  vector<int> Next; //VALUES OF THE NODES THAT FOLLOW THE HEAD
  vector<Nodeoflinkedlist*> vector_pointers; //VECTOR OF NODES
};

// This function reads the input file and creates the adjacent list
void create_list(const string& file, vector<Nodeoflinkedlist*>& adjacent_list){
  ifstream data(file); //reads data from file
  Nodeoflinkedlist* head = NULL;
  Nodeoflinkedlist* next_ptr = NULL;
  int start;
  int end;
  while (data >> start >> end) { //GRABS START AND END OF AN EDGE
    if (start == end){ 
      continue;
    }//END BRANCH THAT CHECKS SELF LOOPS
  vector<Nodeoflinkedlist*>::iterator temp = lower_bound(adjacent_list.begin(), adjacent_list.end(), start, [](Nodeoflinkedlist* i, int id) { return i->ID < id; }); //FINDS NODE WITH START VALUE OR CREATES ONE IF IT DOES NOT EXIST
  if (temp == adjacent_list.end() || (*temp)->ID != start) { //CHECKS IF START VALUE NODE IS IN THE VECTOR OF NODES
    head = new Nodeoflinkedlist{start, vector<int>()}; //CREATES NEW NODE
    adjacent_list.insert(temp, head);//ADDS NODE TO VECTOR
  }//END BRANCH
  else {
    head = *temp;
  }//END BRANCH
  if (find(head->Next.begin(), head->Next.end(), end) == head->Next.end()) {
    head->Next.push_back(end); //ADDS THE END OF EDGE TO NODE
  }//END BRANCH
  temp = lower_bound(adjacent_list.begin(), adjacent_list.end(), end, [](Nodeoflinkedlist* i, int id) {       return i->ID < id; }); //FIND NODE WITH END VALUE OR CREATES ONE IF IT DOES NOT EXIST
  if (temp == adjacent_list.end() || (*temp)->ID != end) {
    next_ptr = new Nodeoflinkedlist{end, vector<int>()}; //CREATES NEW NODE
    adjacent_list.insert(temp, next_ptr); //ADDS NODE TO VECTOR
  }//END BRANCH
else {
    next_ptr = *temp;
}//END BRANCH
    if (find(next_ptr->Next.begin(), next_ptr->Next.end(), start) == next_ptr->Next.end()) { //CHECKS THE START OF THE NEXT EDGE
      next_ptr->Next.push_back(start); //ADDS NODE TO VECTOR
    }//END BRANCH 
  }//END WHILE LOOP
}//END FUNCTION

// This function saves the adjaceny list to a file
void save_to_file(const string& file, vector<Nodeoflinkedlist*>& adjacent_list){
  sort(adjacent_list.begin(), adjacent_list.end(), [](Nodeoflinkedlist* h1, Nodeoflinkedlist* h2) {return h1->ID < h2->ID;}); //SORT NODE IN ASCENDING ORDER
  ofstream data(file); //CREATE AN OUTPUT OBJECT
  for (auto i : adjacent_list) { //ITERATE THROUGH LIST OF NODES
    data << i->ID << ":";
    sort(i->Next.begin(), i->Next.end()); //SORT IN ASCENDING ORDER
    for (auto destination : i->Next) { //ITERATE  THROUGH END VALUES
      data << " " << destination;
    }//END INNER LOOP
    data << endl;
  }//END OUTER LOOP
}//END FUNCTION

// This function prints the stats of the file represented by the adjaceny list
void print_data(vector<Nodeoflinkedlist*>& adjacent_list){
int Nodes;
  int Edges = 0;
  int max_degree = 0;
  for (auto i : adjacent_list) {
    int degree = i->Next.size();//GRABS NUMBER OF DEGREES FOR A SINGLE NODE
    Edges += degree; //ADDS TOTAL SUM OF DEGREES
    if(degree > max_degree){
      max_degree = degree;
    }//END BRANCH
  }//END FOR LOOP
  Nodes = adjacent_list.size();
  Edges /= 2; 
  cout << "Number of nodes: " << Nodes << endl;
  cout << "Number of edges: " << Edges << endl;
  cout << "Maximum degree: " << max_degree << endl;
}

void run(const string& src_path, const string& dst_path) {
  Nodeoflinkedlist test;
  create_list(src_path, test.vector_pointers); 
  save_to_file(dst_path, test.vector_pointers); 
  print_data(test.vector_pointers); 
}

int main() {
  string src_path("karate.txt");
  string dst_path("output.txt");
  run(src_path, dst_path);
}

