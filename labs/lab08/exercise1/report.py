def filter_passing_scores(input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            name, score = line.strip().split(',')
            if int(score) >= 80:
                outfile.write(f"{name},{score}\n")