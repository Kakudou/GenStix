MyAppCSS = """
    Screen {
        border: ascii #004b6f;
        align: center middle;
    }
    Screen > Header {
        background: #004b6f
    }
    Screen > Footer {
        background: #004b6f
    }

    StartScreen {
        border: solid #004b6f;
        height: auto;
    }

    StartScreen > CustomInputField {
        margin-top: 1;
        height: auto;
    }

    StartScreen > Button {
        height: auto;
        width: 100%;
        margin-top: 1;
        background: #004b6f;
    }

    StartScreen > Button:focus {
        background: #004b6f;
        text-style: bold italic;
    }

    #error, .error {
        border: solid red;
        height: auto;
        width: 100%;
        margin-top: 1;
        background: rgb(105,0,0);
        text-style: bold;
        text-align: center;
    }

    YesNoModalScreen, ValidationModal {
       align: center middle;
    }

    #Modal {
        grid-size: 3;
        grid-gutter: 1 3;
        grid-rows: 1fr 3;
        padding: 0 1;
        width: 60;
        height: 11;
        border: thick $background 80%;
        background: $surface;
    }

    #YesNoQuestion, #ValidationModal {
        column-span: 3;
        height: 1fr;
        width: 1fr;
        content-align: center middle;
    }

    Button {
        width: 100%;
    }

    .center-button {
        column-span: 3;
    }

    HomeScreen > NavigationTree {
        dock: left;
        width: 17%;
        height: 100%;
        border: ascii #004b6f;
    }

    HomeScreen > ContentScreen {
        dock: right;
        width: 83%;
        height: 100%;
        color: #004b6f;
        border: ascii #004b6f;
        align: center middle;
    }

    CustomInputField {
        margin-top: 1;
        height: auto;
    }

    AutoComplete {
        height: auto;
    }

    Input {
        margin-top: 1;
        text-style: bold;
        color: #9e9999;
        background: rgb(50, 57, 50);
        border: double #004b6f;
        box-sizing: border-box;
        height: 3;
        position: relative;
    }

    #horizontal-layout {
        layout: horizontal;
        height: auto;

    }
    #horizontal-layout > .hashes_fields {
        width: 50%;
    }
    #horizontal-layout > #hashes_algo_field {
        width: 20%;
    }
    #horizontal-layout > #hashes_value_field {
        width: 80%;
    }

    """
