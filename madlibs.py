def main():
	print("Mad libs where libs get mad.")
	print("Start below:")

	time = input("Enter a number from 1 to 12: ")
	noun = input("Enter a noun (plural): ")
	name = input("Enter a name: ")
	sentence = input("Enter any sentence: ")
	verb = input("Enter a verb: ")

	print("The story goes...")
	output = f"""
	It was {time} o'clock when I heard a knock at the door.
	I opened the door and there was a box full of {noun} with a note saying "From Mr. {name.title()}."
	Just as I closed the door I heard a scream "{sentence.upper()}"
	I froze in place and all I could do was {verb}.
	"""
	print(output)


if __name__ == '__main__':
	main()