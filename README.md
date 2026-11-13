# TMA Workspace

A web application designed to simplify writing Open University mathematics assignments by displaying TMA questions alongside an answer editor.


## Design Decisions

- **Testing:** Use pytest fixtures to avoid repeating setup code, while keeping monkeypatching within individual tests since each test needs different behaviour.
- **Layout:** Display the PDF and text editor side by side to make it easier to move between questions and answers.
- **Question detection:** Start by detecting main question headings (Question 1, Question 2, etc.) and see how useful this is before adding more detailed detection.
