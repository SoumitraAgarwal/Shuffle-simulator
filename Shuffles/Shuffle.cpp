# include <bits/stdc++.h>

using namespace std;

int deck[52] = {0};

int main()
{
	int i;
	ofstream myfile;
	myfile.open ("../Data/init.txt");
	
	for(i = 0; i<52; i++)
	{
		deck[i] = i + 1;
		myfile << i + 1; 
		myfile << "\n";
	}
	myfile.close();


	// Overhand 5 shuffle

	myfile.open ("../Data/Overhand_5.txt");
	int overhand[52];
	copy(deck, deck + 52, overhand);
	for(i = 0; i<10; i++)
	{
		int split = 20 + rand() % 32;
		int temp[52];
		copy(overhand, overhand + 52, temp);
		int j;
		for(j = 0; j<52; j++)
		{
			printf("%d ", temp[j]);
		}
		printf("\n----------\n");
		for(j = 0; j<52; j++)
		{
			printf("%d ", temp[j]);
		}
		printf("\n------------------\n");
		for(j = 0; j<52; j++)
		{
			temp[j] = overhand[(j + split)%52];
		}
		for(j = 0; j<52; j++)
		{
			printf("%d ", temp[j]);
		}
		printf("\n----------\n\n\n\n");
		copy(temp, temp + 52, overhand);
	}	

	for(i = 0; i<52; i++)
	{
		myfile << overhand[i]; 
		myfile << "\n";
	}
	myfile.close();

	return 0;
}