# staT.py

class staT:
    """A class to perform basic statistical operations on both raw and grouped data, with working tables."""

    @staticmethod
    def mean(data, grouped=False):
        """Calculate the mean of the data."""
        if grouped:
            total_frequency = sum(freq for _, freq in data)
            total_sum = sum(midpoint * freq for midpoint, freq in data)
            return total_sum / total_frequency if total_frequency > 0 else 0
        else:
            total = sum(data)
            count = len(data)
            return total / count if count > 0 else 0

    @staticmethod
    def median(data, grouped=False):
        """Calculate the median of the data."""
        if grouped:
            cumulative_frequency = 0
            total_frequency = sum(freq for _, freq in data)
            for midpoint, freq in data:
                cumulative_frequency += freq
                if cumulative_frequency >= total_frequency / 2:
                    return midpoint
        else:
            sorted_data = sorted(data)
            count = len(sorted_data)
            if count % 2 == 0:
                mid1 = count // 2
                mid2 = mid1 - 1
                return (sorted_data[mid1] + sorted_data[mid2]) / 2
            else:
                mid = count // 2
                return sorted_data[mid]

    @staticmethod
    def mode(data, grouped=False):
        """Calculate the mode of the data."""
        if grouped:
            max_frequency = max(freq for _, freq in data)
            mode_values = [midpoint for midpoint, freq in data if freq == max_frequency]
            return mode_values if max_frequency > 0 else None
        else:
            frequency = {}
            for value in data:
                frequency[value] = frequency.get(value, 0) + 1
            
            max_count = max(frequency.values())
            mode_values = [key for key, count in frequency.items() if count == max_count]
            return mode_values if max_count > 1 else None  # return None if there is no mode

    @staticmethod
    def mct(data, grouped=False):
        """Calculate measures of central tendency: mean, median, and mode."""
        mean_value = staT.mean(data, grouped)
        median_value = staT.median(data, grouped)
        mode_value = staT.mode(data, grouped)
        return [mean_value, median_value, mode_value]

    @staticmethod
    def mct_wr(data, grouped=False, return_all=True, return_mean=False, return_median=False, return_mode=False):
        """
        Returns working tables for calculating mean, median, and mode.
        
        Parameters:
        - return_all: If True, returns working tables for mean, median, and mode.
        - return_mean: If True, returns the working table for mean.
        - return_median: If True, returns the working table for median.
        - return_mode: If True, returns the working table for mode.
        """
        working_tables = {}

        # Mean working table
        if return_all or return_mean:
            if grouped:
                total_frequency = sum(freq for _, freq in data)
                total_sum = sum(midpoint * freq for midpoint, freq in data)
                working_tables['mean'] = {
                    'midpoints': [midpoint for midpoint, _ in data],
                    'frequencies': [freq for _, freq in data],
                    'fx': [midpoint * freq for midpoint, freq in data],
                    'total_fx': total_sum,
                    'total_frequency': total_frequency,
                    'mean': total_sum / total_frequency if total_frequency > 0 else 0
                }
            else:
                working_tables['mean'] = {
                    'data': data,
                    'sum': sum(data),
                    'count': len(data),
                    'mean': sum(data) / len(data) if len(data) > 0 else 0
                }

        # Median working table
        if return_all or return_median:
            if grouped:
                cumulative_frequency = 0
                total_frequency = sum(freq for _, freq in data)
                working_tables['median'] = {
                    'midpoints': [midpoint for midpoint, _ in data],
                    'frequencies': [freq for _, freq in data],
                    'cumulative_frequencies': [],
                    'median': None
                }
                for midpoint, freq in data:
                    cumulative_frequency += freq
                    working_tables['median']['cumulative_frequencies'].append(cumulative_frequency)
                    if cumulative_frequency >= total_frequency / 2 and working_tables['median']['median'] is None:
                        working_tables['median']['median'] = midpoint
            else:
                sorted_data = sorted(data)
                count = len(sorted_data)
                if count % 2 == 0:
                    mid1 = count // 2
                    mid2 = mid1 - 1
                    median_value = (sorted_data[mid1] + sorted_data[mid2]) / 2
                else:
                    mid = count // 2
                    median_value = sorted_data[mid]
                working_tables['median'] = {
                    'sorted_data': sorted_data,
                    'median': median_value
                }

        # Mode working table
        if return_all or return_mode:
            if grouped:
                max_frequency = max(freq for _, freq in data)
                mode_values = [midpoint for midpoint, freq in data if freq == max_frequency]
                working_tables['mode'] = {
                    'midpoints': [midpoint for midpoint, _ in data],
                    'frequencies': [freq for _, freq in data],
                    'mode': mode_values if max_frequency > 0 else None
                }
            else:
                frequency = {}
                for value in data:
                    frequency[value] = frequency.get(value, 0) + 1
                max_count = max(frequency.values())
                mode_values = [key for key, count in frequency.items() if count == max_count]
                working_tables['mode'] = {
                    'data': data,
                    'frequencies': frequency,
                    'mode': mode_values if max_count > 1 else None
                }

        return working_tables
