def clean_number(x):
        """ If the value is a string, then remove currency symbol and delimiters
        otherwise, the value is numeric and can be converted
        """
        if isinstance(x, str):
            return(x.replace('$', '').replace(',', '').replace('K', '').replace('M', '').replace('%', ''))
        return(x)