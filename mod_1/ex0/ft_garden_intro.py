# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_garden_intro.py                                 :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: vguerra- <vguerra-@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/02/18 18:02:06 by vguerra-          #+#    #+#              #
#    Updated: 2026/02/20 13:12:09 by vguerra-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def main() -> None:
    """Show the starting plant details."""
    name: str = "Rose"
    height: str = "25cm"
    age: str = "30 days"

    print("=== Welcome to My Garden ===")
    print(f"Plant: {name}")
    print(f"Height: {height}")
    print(f"Age: {age}")
    print("\n=== End of Program ===")

if __name__ == "__main__":
    main()
