#include <iostream>
#include<fstream>

using namespace std;

int main()
{
    string data;
    int sum=0;
    string first="\0";
    string end="\0";
    ifstream readfile("day1_1_data");
    while(getline(readfile, data))
    {
        cout<<data<<endl;

        for(int i=0;i<data.length();i++){
            if(isdigit(data[i]))
            {
                if(first=="\0")
                    first=data[i];
                else
                    end=data[i];
            }
        }
        if(end=="\0")
            end=first;
        sum+= stoi(first)*10+stoi(end);
        cout<<stoi(first)*10+stoi(end)<<endl;
        first="\0";
        end="\0";
    }
    cout<<sum;
}