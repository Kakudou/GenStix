# Not Ready for use
**This project is a work in progress and is not yet ready for use.**

Here is the initial ROADMAP for the project, the goals is a released of a v1 at the end of January 2025.

Roadmap before the V1 release:
   - Create the first CLI for Attack Pattern, Kill Chain Phase and External Reference
   - Create the first TUI for Attack Pattern, Kill Chain Phase and External Reference
   - Create a storage in file in a desired folder in STIX2.1 json format.
   - Finish the contribution guide based on the 3 previous points.
   - Implement all the missing STIX2.1 objects. in the same way (in the order describe later in the README.md)
   - Implenent SRO/Relationship between the objects.
   - Implement the export of the objects in a bundle.
At this point, the project will be ready for a v1 release, but i will also add the following features:
   - Implement the export of the objects in a feed API REST.
   - Implement the export to OpenCTI, through feed or specific connector.

Feel free to post an issue, or contact me by email if you have any question or suggestion.   



# **GenSTIX**  
*A lightweight CLI/TUI tool for generating and bundling STIX 2.1 objects.*

---

<center>  
<a href="https://gitmoji.carloscuesta.me">  
  <img src="https://img.shields.io/badge/gitmoji-%20😜%20😍-FFDD67.svg?style=flat-square" alt="Gitmoji">  
</a>  
</center>

---

## **TL;DR**

GenSTIX is a Python-based CLI/TUI tool for generating and bundling STIX 2.1 objects. It is tailored for researchers, malware analysts, pentesters, and threat intelligence professionals who require quick and offline STIX object creation.

---

- [GenSTIX](#genstix)  
  - [TL;DR](#tl;dr)  
  - [Overview](#overview)  
  - [Features](#features)  
  - [Use Cases](#use-cases)  
  - [Installation](#installation)  
    - [Prerequisites](#prerequisites)  
    - [Installation Steps](#installation-Steps)  
  - [Usage](#usage)  
    - [CLI Mode](#cli-mode)  
    - [TUI Mode](#tui-mode)  
    - [Exporting Bundles](#exporting-Bundles)  
  - [Supported STIX 2.1 Objects](#supported-stix-2.1-objects)  
    - [STIX Domain Objects (SDOs)](#stix-domain-objects-(sdos))  
    - [STIX Relationship Objects (SROs)](#stix-relationship-objects-(sros))  
    - [STIX Cyber-observable Objects (SCOs)](#stix-cyber-observable-objects-(scos))  
    - [STIX Open Vocabulary Objects (ov)](#stix-open-vocabulary-objects-(ov))  
    - [STIX Common Data Types (CDTs)](#stix-common-data-types-(cdts))  
    - [Bundles](#bundles)  
    - [Enums](#enums)  
  - [Roadmap](#roadmap)  
  - [Contributing](#contributing)  
  - [Architecture](#architecture)  
    - [Clean Architecture](#clean-architecture)  
    - [BDD (Behavior-Driven Development)](#bdd-(behavior-driven-development))  
    - [TDD (Test-Driven Development)](#tdd-(test-driven-development))  
    - [DDD (Domain-Driven Design)](#ddd-(domain-driven-design))  
    - [Port/Adapter Pattern](#portadapter-pattern)  
    - [Builder Pattern](#builder-pattern)  
  - [Example for a new Feature](#example-for-a-new-feature)  
  - [License](#license)  
    - [Happy STIXing!](#happy-stixing)  

---

## **Overview**  

GenSTIX is a Python-based CLI/TUI tool designed to simplify the creation of STIX 2.1 objects and bundles. Whether you're in an air-gapped environment, working on a lightweight Linux server, or simply want a seamless way to create valid STIX objects, GenSTIX provides an intuitive and powerful solution.

---

## **Features**  
- **Interactive Object Creation**: Intuitive CLI/TUI interface to generate STIX 2.1 objects such as Indicators, Threat Actors, Malware, etc.  
- **Bundle Support**: Easily combine multiple objects into a valid STIX 2.1 bundle.  
- **Offline-First**: Works without an internet connection, perfect for air-gapped environments.  
- **JSON Export**: Export your STIX objects and bundles in JSON format for compatibility with systems like [OpenCTI](https://filigran.io/solutions/open-cti/) and others.  
- **Cross-Platform**: Compatible with Linux, macOS, and Windows with minimal dependencies.  
- **Extensibility**: Built to support additional STIX objects and custom attributes with ease.  
- **Create API Feeds**: Generate a feed of STIX objects for seamless integration with threat intelligence platforms.  
- **Open Source**: Licensed under MIT, encouraging contributions and modifications.  

---

## **Use Cases**

1. **Training & Education**: Practice building STIX 2.1 objects interactively to better understand their structure and purpose.  
2. **Threat Intel Sharing**: Quickly create Indicators or Threat Actors for internal or external collaboration.  
3. **Malware Analysis**: Generate and export malware-related STIX objects during investigations in sandboxed or offline environments.  
4. **Pentesting Reports**: Document findings in STIX format to integrate into organizational threat intelligence systems.  

---

## **Installation**  

### **Prerequisites**  
- Python 3.13 or later  
- `pip` (Python package installer)  
- `venv` (Python virtual environment)  

### **Installation Steps**  

1. Clone the repository and access the folder:  
   ```bash
   git clone https://github.com/kakudou/GenStix.git
   cd GenStix
   ```  

2. Create and activate a virtual environment:  
   ```bash
   python -m venv .venv --prompt=GenSTIX
   source .venv/bin/activate 
   ```  

3. Install the required dependencies:  
   ```bash
   pip install .
   ```  

4. Run the tool:  
   ```bash
   GenSTIX
   ```  

later on, we will release the package to PyPi for easier installation.

---

## **Usage**

### **CLI Mode**  
1. Launch the tool:  
   ```bash
   GenSTIX
   ```  
2. Follow the interactive prompts to create STIX objects.

### **TUI Mode**  
1. Launch the tool in TUI mode:  
   ```bash
   GenSTIX --tui
   ```  
2. Navigate through menus to select object types, populate attributes, and manage bundles.  

### **Exporting Bundles**  
After creating objects, you can bundle and export them as JSON for further use in threat intel platforms.  

---

## **Supported STIX 2.1 Objects**  

### **STIX Domain Objects (SDOs)**  
- [x] Attack Pattern
- [ ] Campaign  
- [ ] Course of Action  
- [ ] Grouping  
- [ ] Identity  
- [ ] Indicator  
- [ ] Infrastructure  
- [ ] Intrusion Set  
- [ ] Location  
- [ ] Malware Analysis  
- [ ] Malware  
- [ ] Note  
- [ ] Observed Data  
- [ ] Opinion  
- [ ] Report  
- [ ] Threat Actor  
- [ ] Tool  
- [ ] Vulnerability  

### **STIX Relationship Objects (SROs)**  
- [ ] Relationship  
- [ ] Sighting  

### **STIX Cyber-observable Objects (SCOs)**  
- [ ] Artifact  
- [ ] Autonomous System  
- [ ] Directory  
- [ ] Domain Name  
- [ ] Email Address  
- [ ] Email Message  
- [ ] File  
- [ ] IPv4 Address  
- [ ] IPv6 Address  
- [ ] MAC Address  
- [ ] Mutex  
- [ ] Network Traffic  
- [ ] Process  
- [ ] Software  
- [ ] URL  
- [ ] User Account  
- [ ] Windows Registry Key  
- [ ] X.509 Certificate  

### **STIX Open Vocabulary Objects (ov)**

- [x] Hashing Algorithm Vocabulary

### **STIX Common Data Types (CDTs)**

- [x] External Reference
- [x] Kill Chain Phase
- [ ] Hashes

### **Bundles**  
- [ ] Bundle  

### **Enums**
- [x] External Reference CAPEC

---

## **Roadmap**  
1. **Validation**: Automate validation for compliance with the STIX 2.1 specification.  
2. **Enhanced TUI**: Build a richer, more interactive terminal UI for easier navigation.  
3. **Custom Templates**: Enable users to save and reuse common attribute templates.  
4. **Documentation**: Develop comprehensive guides with step-by-step examples.  
5. **Integration Features**: Allow exporting to external threat intel APIs and feeds.  

---

## **Contributing**

We welcome contributions from the community! Here's how to get involved:  
1. Fork the repository and create a feature branch.  
2. Make your changes and ensure they align with the project's architecture (see below).  
3. Submit a pull request with a detailed description of your changes.  
4. Open issues or suggest features in the [Issues](https://github.com/kakudou/genstix/-/issues) section.  

---

## **Architecture**  

GenSTIX adheres to modern software development principles to ensure scalability, maintainability, and ease of collaboration. Below are the core architectural choices:  


### **Clean Architecture**  
Clean Architecture organizes software into layers, separating high-level policy (business logic) from low-level implementation details (frameworks, databases, etc.). Core components are independent of external dependencies, promoting testability, scalability, and adaptability.

### **BDD (Behavior-Driven Development)**  
BDD emphasizes collaboration between developers, testers, and stakeholders to define behavior and requirements using natural language. It bridges communication gaps and ensures the software meets business goals by focusing on user-driven scenarios and acceptance criteria.

### **TDD (Test-Driven Development)**  
TDD focuses on writing tests before implementation. It involves a cycle of writing a failing test, implementing the code to pass the test, and then refactoring. This ensures code correctness, reduces defects, and improves overall design.

### **DDD (Domain-Driven Design)**  
DDD is a design approach centered on the core business domain. It uses a shared, ubiquitous language between developers and stakeholders, defining clear boundaries between domain logic and other concerns through strategic design patterns.

### **Port/Adapter Pattern**  
This pattern decouples the core application logic from external systems (like databases or APIs) through defined interfaces. Ports represent abstractions of core functionality, while adapters implement these abstractions for specific technologies or use cases.

### **Builder Pattern**  
The Builder Pattern constructs complex objects step by step, separating object creation from its representation. It provides flexibility and clarity when dealing with optional parameters, validation, or different configurations.


## **Example for a new Feature**

Follow the guide at [CONTRIBUTING.md](CONTRIBUTING.md) to add a new feature or object to GenSTIX.

---

## **License**  

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.  

---

<center><sub>✨ Made with ❤️ by [Kakudou ~ カクドウ](https://kakudou.org) ✨</sub></center>  

--- 

### **Happy STIXing!**  
