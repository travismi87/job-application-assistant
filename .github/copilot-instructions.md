# Custom GitHub Copilot Instructions (Full-Stack)

### General Instructions (For All Code)
- Always prioritize **readability, maintainability, and scalability**.
- Write code with good design practices, including comments on *why* certain architectural decisions were made.
- For complex algorithms or logic, include comments explaining the approach used.
- Handle edge cases gracefully and implement clear exception handling.
- For libraries or external dependencies, mention their usage and purpose in comments.
- Use consistent, descriptive naming conventions that reveal intent.

### Python Backend Instructions
- **Code Style:** Follow the **PEP 8** style guide, using a line length of **88 characters** to align with modern formatters like `black` and `ruff`. Use 4 spaces for indentation.
- **Clarity:**
    - Write clear and concise comments for each function.
    - Ensure functions have descriptive names and include full type hints using the `typing` module (e.g., `List[str]`).
    - Provide docstrings for all modules, classes, and functions following **PEP 257** conventions.
- **Architecture:**
    - Break down complex functions into smaller, single-purpose functions.
    - Adhere to the layered architecture (`api`, `services`, `crud`) we've designed.

### Next.js/TypeScript Frontend Instructions
- **Code Style:** Follow the **Prettier** configuration defined in the project. Use 2 spaces for indentation.
- **Clarity:**
    - Write clear and concise comments for complex components or custom hooks.
    - Use descriptive names for components (PascalCase), hooks (useSomething), and variables (camelCase).
    - Use **TypeScript** for all code. Avoid `any` and strive for strong type safety. Define clear `interface` or `type` definitions for props and API data structures.
- **Architecture & Best Practices:**
    - **Component Design:** Build small, reusable, single-purpose components. Favor composition over inheritance.
    - **State Management:** Adhere to the established state management pattern:
        - **Tanstack Query:** Use for ALL server state (fetching, caching, mutations).
        - **Zustand:** Use ONLY for minimal, global UI state (e.g., theme, auth status).
    - **Hooks:** Encapsulate reusable logic, especially for side effects, in custom hooks.

### Edge Cases and Testing
- **Backend:** Write unit tests for services and critical paths using `pytest`. Account for common edge cases like empty inputs and invalid data.
- **Frontend:** Write tests for components and custom hooks using **Jest** and **React Testing Library**. Test for different states (loading, error, success) and user interactions.
- Document tests with comments explaining the specific cases being tested.

### Example of Proper Documentation (Python)
```python
def calculate_area(radius: float) -> float:
    """Calculates the area of a circle given its radius.

    Args:
        radius (float): The radius of the circle. Must be a non-negative number.

    Returns:
        float: The area of the circle, calculated as π * radius².

    Raises:
        ValueError: If the radius is negative.
    """
    if radius < 0:
        raise ValueError("Radius cannot be negative.")
    import math
    return math.pi * radius ** 2