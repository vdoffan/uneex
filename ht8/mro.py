def main():
    import sys

    # Read input lines using the specified loop
    code_lines = []
    while True:
        try:
            line = input()
            if line == '':
                break
            code_lines.append(line)
        except EOFError:
            break  # End of input

    # Initialize defined_classes with 'object' since it's predefined
    defined_classes = {'object'}
    classes = {}  # Dictionary to store class inheritance: class_name -> list of base classes

    for line in code_lines:
        stripped_line = line.lstrip()  # Remove leading whitespace
        if not stripped_line.startswith('class '):
            # Skip lines that do not start with 'class '
            continue

        # Remove 'class ' prefix
        class_def = stripped_line[6:]
        colon_pos = class_def.find(':')
        if colon_pos == -1:
            # Invalid class definition without ':'
            print('No')
            return

        before_colon = class_def[:colon_pos].strip()

        # Check if there are base classes specified
        if '(' in before_colon:
            paren_start = before_colon.find('(')
            paren_end = before_colon.find(')', paren_start)
            if paren_end == -1:
                # Invalid class definition without closing ')'
                print('No')
                return

            class_name = before_colon[:paren_start].strip()
            bases_str = before_colon[paren_start + 1:paren_end].strip()
            base_classes = [base.strip() for base in bases_str.split(',') if base.strip()] if bases_str else ['object']
        else:
            class_name = before_colon.strip()
            base_classes = ['object']

        if class_name in classes:
            # Duplicate class definition
            print('No')
            return

        # Ensure all base classes are already defined
        if any(base not in defined_classes for base in base_classes):
            print('No')
            return

        # Register the class
        classes[class_name] = base_classes
        defined_classes.add(class_name)

    # Predefine MRO for 'object'
    mro_dict = {'object': ['object']}

    # Function to compute MRO using C3 linearization
    def compute_mro(cls_name):
        if cls_name in mro_dict:
            return mro_dict[cls_name]
        base_classes = classes[cls_name]
        mro_lists = [compute_mro(base) for base in base_classes]
        mro_lists.append(base_classes)
        mro = merge(mro_lists)
        mro_dict[cls_name] = [cls_name] + mro
        return mro_dict[cls_name]

    # Merge function as per C3 linearization
    def merge(seqs):
        result = []
        while True:
            seqs = [seq for seq in seqs if seq]  # Remove empty sequences
            if not seqs:
                return result
            for seq in seqs:
                candidate = seq[0]
                if not any(candidate in s[1:] for s in seqs):
                    break
            else:
                # Inconsistent hierarchy
                raise ValueError("Inconsistent hierarchy")
            result.append(candidate)
            for seq in seqs:
                if seq[0] == candidate:
                    del seq[0]

    try:
        for cls_name in classes:
            compute_mro(cls_name)
    except ValueError:
        print('No')
        return

    print('Yes')


if __name__ == "__main__":
    main()
