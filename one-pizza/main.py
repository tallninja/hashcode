# You are opening a small pizzeria.
# In fact, your pizzeria is so small that you decided to offer only one type of pizza.
# Now you need to decide what ingredients to include (peppers? tomatoes? both?).
# Everyone has their own pizza preferences. 
# Each of your potential clients has some ingredients they like, and maybe some ingredients they dislike. 
# Each client will come to your pizzeria if both conditions are true:


def get_final_ingredients(data):
    likes = []
    dislikes = []
    ingredients = set()
    number_of_potential_clients = int(data[0])
    clients_preferences = data[1:]
    assert number_of_potential_clients * 2 == len(clients_preferences)
    for i in range(0, len(clients_preferences), 2):
        likes.extend(clients_preferences[i].split(' ')[1:])
        dislikes.extend(clients_preferences[i + 1].split(' ')[1:])

    for like in likes:
        if like not in dislikes:
            ingredients.add(like)

    output = f'{len(ingredients)}'

    for ingredient in ingredients:
        output += f' {ingredient}'

    return output

def main():
    data = []
    
    with open('e_elaborate.in.txt', 'r') as input_file:
        data = input_file.read().strip().split('\n')

    final_ingredients = get_final_ingredients(data)
    print(final_ingredients)
    

if __name__ == '__main__':
    main()