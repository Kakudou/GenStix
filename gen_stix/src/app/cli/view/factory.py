"""This module will contain factory functions for creating objects usefull in the CLI"""

import questionary
from questionary import Separator
from math import ceil


class Factory:

    @staticmethod
    def paginated_list_factory(list_to_paginate, title):
        if len(list_to_paginate) > 0:
            min_elmnt = 0
            max_elmnt = len(list_to_paginate)
            paginate = 5

            actual_page = 0
            first_elmnt = min_elmnt
            last_elemnt = paginate if max_elmnt >= paginate else max_elmnt

            number_page = int(ceil(max_elmnt / paginate) - 1)

            all_objects = [x.strip() for x in list_to_paginate]

            object_name = "Get next"
            while ("Get next" in object_name) or (
                "Get previous" in object_name
            ):

                choices = []
                if number_page > 0:
                    if actual_page > 0:
                        choices.append("Get previous")
                    if actual_page != number_page:
                        choices.append("Get next")

                if number_page > 0:
                    choices.append(
                        Separator(
                            f"-= Pages {actual_page + 1}/{number_page + 1} =-\n"
                        )
                    )
                choices.append(Separator(f"-= {title} =-\n"))
                choices.extend(all_objects[first_elmnt:last_elemnt])

                object_name = questionary.select(
                    "Select one in all of that:",
                    choices=choices,
                    use_shortcuts=True,
                    use_arrow_keys=True,
                ).ask()

                if "Get next" in object_name:
                    actual_page = (
                        actual_page + 1
                        if actual_page + 1 < number_page
                        else number_page
                    )
                elif "Get previous" in object_name:
                    actual_page = actual_page - 1 if actual_page - 1 > 0 else 0

                first_elmnt = 5 * actual_page
                last_elemnt = (
                    (5 * actual_page + paginate)
                    if (5 * actual_page + paginate) <= max_elmnt
                    else max_elmnt
                )

                return object_name
