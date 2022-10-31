def read_samples(file_path):
    """ reading unique sample names into list """

    with open(file_path) as f:
        sample_names = f.read().splitlines()

    return(sample_names)
