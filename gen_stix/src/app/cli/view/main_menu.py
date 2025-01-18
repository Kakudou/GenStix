"""This module is the main menu of the application."""

import questionary
from sys import exit
from gen_stix.src.app.cli.view.factory import Factory


class MainMenu:

    cdts = [
        "Kill Chain Phase",
        # ?         "External Reference",
        # ?         "Hashes",
    ]

    sdos = [
        # ?         "Attack Pattern",
        # ?         "Campaign",
        # ?         "Course of Action",
        # ?         "Identity",
        # ?         "Indicator",
        # ?         "Intrusion Set",
        # ?         "Location",
        # ?         "Malware Analysis",
        # ?         "Malware",
        # ?         "Note",
        # ?         "Observed Data",
        # ?         "Opinion",
        # ?         "Report",
        # ?         "Threat Actor",
        # ?         "Tool",
        # ?         "Vulnerability",
    ]

    sros = [
        # ?         "Relationship",
        # ?         "Sighting",
    ]

    scos = [
        # ?         "Artifact",
        # ?         "Autonomous System",
        # ?         "Directory",
        # ?         "Domain Name",
        # ?         "Email Address",
        # ?         "Email Message",
        # ?         "File",
        # ?         "IPv4 Address",
        # ?         "IPv6 Address",
        # ?         "MAC Address",
        # ?         "Mutex",
        # ?         "Network Traffic",
        # ?         "Process",
        # ?         "Software",
        # ?         "URL",
        # ?         "User Account",
        # ?         "Windows Registry Key",
        # ?         "X509 Certificate",
    ]

    @staticmethod
    def show(
        referer=None, project_name=None, projects_path=None, type_stix=None
    ):
        if referer is None:
            if type_stix is None:
                type_stix = MainMenu.select_cat_stix()

            print(
                f"\r\nThe action selected is to manage the STIX2.1 type: {type_stix}\r\n"
            )
            choices = [
                f"Create '{type_stix}'",
                f"Read '{type_stix}'",
                f"Update '{type_stix}'",
                f"Delete '{type_stix}'",
                "Exit",
            ]

            if type_stix in MainMenu.cdts:
                choices.remove(f"Update '{type_stix}'")

            crudl_operation = questionary.select(
                f"What CRUDL operation do you want to perform on {type_stix}?",
                choices=choices,
                use_shortcuts=True,
                use_arrow_keys=True,
            ).ask()
            if crudl_operation == "Exit":
                exit(0)
        else:
            crudl_operation = referer
            type_stix = referer.split("'")[1].split("'")[0]

        if type_stix in MainMenu.sdos:
            cat_stix = "sdos"
        elif type_stix in MainMenu.scos:
            cat_stix = "scos"
        elif type_stix in MainMenu.sros:
            cat_stix = "sros"
        elif type_stix in MainMenu.cdts:
            cat_stix = "cdts"

        class_to_call = f"{crudl_operation.replace(' ', '').replace("'", '')}"
        print(f"\r\nThe CRUDL operation selected is: {crudl_operation}\r\n")

        file_name = (
            f"{crudl_operation.replace(' ', '_').replace("'", '').lower()}"
        )

        path = f"gen_stix.src.app.cli.view.{cat_stix}.{type_stix.replace(' ', '_').lower()}.{file_name}"
        module = __import__(path, fromlist=[class_to_call])
        class_ = getattr(module, class_to_call)
        class_.show(project_name, projects_path)

    @staticmethod
    def select_cat_stix():
        # for item in all ths lists above
        list_actions = []

        if len(MainMenu.sdos) > 0:
            list_actions.append("STIX Domain Objects (SDOs)")
        if len(MainMenu.scos) > 0:
            list_actions.append("STIX Cyber Observables (SCOs)")
        if len(MainMenu.sros) > 0:
            list_actions.append("STIX Relationships (SROs)")
        if len(MainMenu.cdts) > 0:
            list_actions.append("Common Data Types (CDTs)")

        type_stix = questionary.select(
            "What do you want to manage?", choices=list_actions
        ).ask()

        cat_stix = ""
        if type_stix == "STIX Domain Objects (SDOs)":
            cat_stix = "sdos"
        elif type_stix == "STIX Cyber Observables (SCOs)":
            cat_stix = "scos"
        elif type_stix == "STIX Relationships (SROs)":
            cat_stix = "sros"
        elif type_stix == "Common Data Types (CDTs)":
            cat_stix = "cdts"

        type_stix = MainMenu.select_type_stix(cat_stix)
        return type_stix

    @staticmethod
    def select_type_stix(cat_stix):

        list_actions = []
        if cat_stix == "sdos":
            list_actions = MainMenu.sdos
        elif cat_stix == "scos":
            list_actions = MainMenu.scos
        elif cat_stix == "sros":
            list_actions = MainMenu.sros
        elif cat_stix == "cdts":
            list_actions = MainMenu.cdts
        else:
            list_actions = (
                MainMenu.sdos + MainMenu.scos + MainMenu.sros + MainMenu.cdts
            )

        type_stix = Factory.paginated_list_factory(
            list_actions, "STIX2.1 Types"
        )

        return type_stix
