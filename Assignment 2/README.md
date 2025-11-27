https://github.com/cp1404-students/a2-books-SwikarM
# CP1404 Assignment 2: Books To Read 2.0 by Swikar Mainali

This project involves creating a book management application with both console and GUI interfaces using object-oriented 
programming principles in Python with Kivy.

## 1. How many hours did you spend working on this assignment 2 project?

I spent approximately 15-18 hours working on this assignment. The breakdown was:
- 4 hours on class design and implementation (Book and BookCollection)
- 2 hours on comprehensive unit testing
- 3 hours converting the console program to use the new classes
- 6-7 hours on Kivy GUI development, including layout design and event handling
- 2 hours on debugging, integration testing, and documentation
- 1 hour on final refinements and submission preparation

The GUI development took the most time due to the learning curve with Kivy's widget system and debugging layout issues.

## 2. What are you most satisfied with?

I'm most satisfied with the successful implementation of the object-oriented design and how it enabled code reuse between
the console and GUI programs. The clean separation between the Book/BookCollection classes and the user interfaces 
strong software architecture principles. I'm particularly proud of how the sorting functionality works consistently across
both interfaces and the robust error handling that provides clear user feedback. The color-coded book buttons in the GUI that
differentiate between unread, completed, and long books create an intuitive user experience that exceeded the basic requirements.

## 3. What are you least satisfied with?

I'm least satisfied with the initial approach to Kivy layout management. I spent considerable time debugging KV file loading
issues and widget positioning that could have been avoided with better upfront planning. The process of dynamically creating 
and managing book buttons in the GUI also proved more complex than anticipated, leading to some code duplication in the event 
handling. Additionally, while the error checking works correctly, the validation logic could be more centralized and reusable
across both interfaces rather than being partially duplicated.

## 4. What worked well in your development process?

The incremental development approach worked exceptionally well. Starting with the Book class, then BookCollection, followed by
tests, then the console program, and finally the GUI created a solid foundation at each stage. Writing unit tests alongside class
development helped catch bugs early and ensured each component worked correctly before integration. Using Git with descriptive 
commit messages allowed me to track progress and revert changes when needed. The decision to embed the KV layout directly in
the Python code once external file loading proved problematic was a turning point that significantly improved development efficiency.

## 5. What about your process could be improved the next time you do a project like this?

For future projects, I would implement several key improvements:
- Create detailed wireframes and component diagrams before writing any GUI code
- Adopt a true test-driven development approach by writing tests before implementation
- Break down the GUI development into smaller, more testable components
- Use Kivy's debugging tools more systematically from the start
- Allocate dedicated time for code review and refactoring throughout the process
- Create a more comprehensive testing plan that includes edge cases and user interaction scenarios
- Start the most challenging components (like GUI development) earlier to allow for unexpected complications

## 6. Describe what learning resources you used and how you used them.

I utilized multiple learning resources strategically:
CP1404 Programming Patterns: Used extensively for menu structures, error checking patterns, and code organization standards
- Kivy Documentation: Referenced for understanding widget properties, event handling, and KV language syntax
- Kivy Demos from Practicals: Studied dynamic_widgets.py for button creation and guitars_app.py for object-oriented GUI design
- PyCharm Debugger: Used to step through Kivy initialization and identify widget loading issues
- Python Official Documentation: Consulted for JSON handling and class method best practices
- Peer Discussions: Engaged with classmates to troubleshoot common Kivy challenges and share solutions

These resources helped me understand not just how to make things work, but why certain approaches are preferred in professional
development.

## 7. Describe the main challenges or obstacles you faced and how you overcame them.

The most significant challenge was the Kivy widget initialization timing issue where `self.root.ids` was empty during the 
initial setup. This caused persistent crashes until I implemented the Clock.schedule_once approach to delay the initial display update.
Another major obstacle was understanding Kivy's property binding system and ensuring the GUI updated correctly when book statuses changed.
overcame this by studying Kivy's observable properties and implementing proper data binding between the collection and the display.

The dynamic button creation for books also presented challenges in managing object references and ensuring click events were properly
handled. I solved this by storing Book objects directly on the button instances and creating a unified event handler. Finally, ensuring
consistent data persistence between the console and GUI programs required careful attention to the JSON serialization/deserialization
process, which I verified through extensive integration testing.

These challenges taught me valuable lessons about framework-specific patterns and the importance of understanding the underlying 
architecture before implementing complex features.