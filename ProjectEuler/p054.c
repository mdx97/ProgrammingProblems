#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct card 
{
	int number;
	char suit;
};

typedef struct card Card;

int get_winner(char *player1_hand, char *player2_hand);
int get_score(Card *cards);
void build_hand(char *hand, Card *cards);
void read_games(const char *file_path, char ***games, int count);
void concatenate(char **str1, char *str2);
void sort(int *arr, int size);
void swap(int *arr, int idx1, int idx2);

int main(int argc, char *argv[])
{
	const int GAMES_COUNT = 1000;
	const char *FILE_PATH = "files/p054_poker.txt";
	
	int i;

	char ***games = malloc(GAMES_COUNT * sizeof(char **));
	for (i = 0; i < GAMES_COUNT; i++)
		games[i] = malloc(2 * sizeof(char *));

	read_games(FILE_PATH, games, GAMES_COUNT);
	
	int winner = 0;
	int player1_wins = 0;
	for (i = 0; i < GAMES_COUNT; i++)
	{
		winner = get_winner(games[i][0], games[i][1]);
		if (winner == 1)
			player1_wins++;
	}
	
	printf("Number of hands player 1 wins: %d\n", player1_wins);
	return 0;
}

int get_winner(char *player1_hand, char *player2_hand)
{
	Card *player1_cards = malloc(5 * sizeof(Card));
	Card *player2_cards = malloc(5 * sizeof(Card));	
	
	build_hand(player1_hand, player1_cards);
	build_hand(player2_hand, player2_cards);

	int player1_score = get_score(player1_cards);
	int player2_score = get_score(player2_cards);
	
	// DEBUG
	//printf("P1: %d | P2: %d\n", player1_score, player2_score);

	int winner = 0;

	if (player1_score > player2_score)
	{
		winner = 1;
	}
	else if (player2_score > player1_score)
	{
		winner = 2;
	}
	else
	{
		// TODO: Resolve situations where score is equal.
	}
	
	free(player1_cards);
	free(player2_cards);

	return winner;
}

// Scores will be represented by these values:
// 9 - Royal Flush
// 8 - Straight Flush
// 7 - Four of a Kind
// 6 - Full House
// 5 - Flush
// 4 - Straight
// 3 - Three of a Kind
// 2 - Two Pairs
// 1 - One Pair
// 0 - Nothing/High Card
int get_score(Card *cards)
{
	int i;
	int *card_numbers = malloc(5 * sizeof(int));
	for (i = 0; i < 5; i++)
		card_numbers[i] = cards[i].number;

	sort(card_numbers, 5);
	
	// Initialize score assuming the hand has nothing
	int score = 0;
	
	// Use DP to get pairs, 3 of a kind, and 4 of a kind.
	int pair1 = 0;
	int pair2 = 0;
	int thok = 0;
	int fok = 0;

	int *dp = malloc(5 * sizeof(int));
	dp[0] = 1;

	for (i = 1; i < 5; i++)
	{
		if (card_numbers[i - 1] == card_numbers[i])
			dp[i] = dp[i - 1] + 1;
			
	}

	for (i = 0; i < 5; i++)
	{
		if (dp[i] == 2)
		{
			if (pair1 == 0)
				pair1 = card_numbers[i];
			else
				pair2 = card_numbers[i];
		}

		if (dp[i] == 3)
			thok = card_numbers[i];
		
		if (dp[i] == 4)
			fok = card_numbers[i];
	}
	
	// Check for pair.
	if (pair1 != 0)
		score = 1;

	// Check for two pairs.
	if (pair1 != 0 && pair2 != 0)
		score = 2;

	// Check for three of a kind.
	if (thok != 0)
		score = 3;

	// Check for straight.
	int has_straight = 1;
	int last_num = 0;
	for (i = 0; i < 5; i++)
	{
		if (last_num != 0)
		{
			if (card_numbers[i] != (last_num + 1))
			{
				has_straight = 0;
				break;
			}
		}

		last_num = card_numbers[i];
	}
	
	if (has_straight)
		score = 4;

	// Check for flush.
	int has_flush = 1;
	char assumed_suit = '\0';
	for (i = 0; i < 5; i++)
	{
		if (assumed_suit != '\0')
		{
			if ((cards[i]).suit != assumed_suit)
			{
				has_flush = 0;
				break;
			}
		}
		else
		{
			assumed_suit = (cards[i]).suit;
		}
	}

	if (has_flush)
		score = 5;
	
	// Check for Full House
	if (thok != 0 && pair1 != 0)
		score = 6;

	// Check for Four of a Kind
	if (fok != 0)
		score = 7;

	// Check for straight flush.
	if (has_straight && has_flush)
		score = 8;

	// Check for royal flush.
	if (has_straight && has_flush && card_numbers[0] == 10)
		score = 9;
	
	// Free allocated memory.
	free(card_numbers);
	free(dp);

	return score;
}

void build_hand(char *hand, Card *cards)
{
	int i = 0;
	char *new_str = strtok(hand, " ");
	while (new_str != NULL)
	{
		Card card;
		char card_val = new_str[0];
		int card_num = 0;

		switch (card_val)
		{
			case 'A':
				card_num = 14;
				break;
			case 'K':
				card_num = 13;
				break;
			case 'Q':
				card_num = 12;
				break;
			case 'J':
				card_num = 11;
				break;
			case 'T':
				card_num = 10;
				break;
			default: {
				char *str = malloc(2 * sizeof(char));
				str[0] = card_val;
				str[1] = '\0';
				card_num = atoi(str);
				free(str);
			}
		}
		
		card.number = card_num;
		card.suit = new_str[1];

		cards[i] = card;
		new_str = strtok(NULL, " ");

		i++;
	}
}

void read_games(const char *file_path, char ***games, int count)
{
	FILE *file_ptr;
	char *line = NULL;
	size_t length = 0;

	file_ptr = fopen(file_path, "r");

	int iter = 0;

	while (iter < count)
	{
		getline(&line, &length, file_ptr);
		char **cards = malloc(10 * sizeof(char *));
		char *new_str = strtok(line, " ");
		int c = 0;

		while (new_str != NULL)
		{
			cards[c] = new_str;
			new_str = strtok(NULL, " ");
			c++;
		}


		int i;
		char *player1_hand = "";
		char *player2_hand = "";
		
		for (i = 0; i < 5; i++)
		{
			if (i > 0)
				concatenate(&player1_hand, " ");
			concatenate(&player1_hand, cards[i]);
		}

		for (i = 5; i < 10; i++)
		{
			if (i > 5)
				concatenate(&player2_hand, " ");
			concatenate(&player2_hand, cards[i]);
		}
	
		games[iter][0] = player1_hand;
		games[iter][1] = player2_hand;
		free(cards);
		iter++;
	}
}

void concatenate(char **str1, char *str2)
{
	int new_size = strlen(*str1) + strlen(str2);
	char *temp = malloc(new_size * sizeof(char));
	strcpy(temp, *str1);
	strcat(temp, str2);
	free(*str1);
	*str1 = malloc(new_size * sizeof(char));
	strcpy(*str1, temp);
	free(temp);
}

void sort(int *arr, int size)
{
	int swaps = 1;
	while (swaps > 0)
	{
		swaps = 0;
		for (int i = 0; i < size - 1; i++)
		{
			if (arr[i] > arr[i + 1])
			{
				swap(arr, i, i + 1);
				swaps++;
			}
		}
	}
}

void swap(int *arr, int idx1, int idx2)
{
	int temp = arr[idx1];
	arr[idx1] = arr[idx2];
	arr[idx2] = temp;
}
