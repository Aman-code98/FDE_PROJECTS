     else:
            # Format: September 8, 1636
            parts = date.split(" ")
            month = months.index(parts[0]) +1   # blank 1 — convert month name to number using months list
            day = int(parts[1].replace(",", ""))
            year = int(parts[2])

        if month >12 or day > 31 :  # blank 2 — validate month and day # This will skip all the below code and go back to the top. other approach is on lined 124.
            continue
            
        print(f"{year:04}-{month:02}-{day:02}")
        break

    except (ValueError, IndexError):
        continue