class PackageHandler:
    package_types = [
        {"type": "small", "height": 150, "length": 200, "breadth":300, "cost":5},
        {"type": "medium", "height": 200, "length": 300, "breadth":400, "cost":7.5},
        {"type": "large", "height": 250, "length": 400, "breadth":600,"cost":8.5}
    ]
    # Ideally we would pull this from a settings file, or a database, etc...

    def validate_input(self, dimensions, weight):
        """Validate whether all the inputs are valid, and throws errors if they are not."""
        if len(dimensions) != 3:
            raise ValueError("The dimensions must contain exactly three elements.")
        if any(dimension for dimension in dimensions if dimension <= 0 ) or weight <= 0:
            raise ValueError("The dimensions or weight must be a positive value.")

    def get_package_type(self, dimensions, weight):
        """Returns the package required for the given dimensions and weight. Returns None if no package type can be matched."""
        self.validate_input(dimensions, weight)

        if weight > 25:
            return None

        # Sorts the dimensions from smallest to largest, and names them height, length, breadth in order.
        dimensions.sort()
        height,length,breadth = tuple(dimensions)

        # Finds the first package type (from smallest to largest) satisfying the dimensions and weight criteria.
        package = next((package for package in self.package_types if  length <= package["length"] and breadth <= package["breadth"] and height <= package["height"]), None)
        return(package)
