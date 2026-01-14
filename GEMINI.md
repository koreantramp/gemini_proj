# Project Context: Todo App

## Overview
This is a single-page Todo application built with **React 19**, **TypeScript**, and **Vite**. It features a modern, responsive UI styled with **Tailwind CSS**. The application allows users to manage their daily tasks with persistence via local storage.

## Tech Stack
*   **Framework:** React 19 (`react`, `react-dom`)
*   **Language:** TypeScript
*   **Build Tool:** Vite (`@vitejs/plugin-react`)
*   **Styling:** Tailwind CSS 4 (via PostCSS)
*   **Linting:** ESLint with React and TypeScript configurations

## Project Structure
*   `src/App.tsx`: Main application logic and UI.
*   `src/main.tsx`: Entry point.
*   `src/index.css`: Tailwind directives and global styles.
*   `vite.config.ts`: Vite configuration.
*   `package.json`: Dependencies and scripts.

## Operational Commands

| Command | Description |
| :--- | :--- |
| `npm run dev` | Starts the development server. |
| `npm run build` | Runs type checks (`tsc`) and builds for production. |
| `npm run lint` | Runs ESLint checks. |
| `npm run preview` | Previews the production build. |

---

## Engineering Standards & Conventions

The following guidelines govern development within this project.

### JavaScript/TypeScript
*   **Plain Objects over Classes:** Prioritize plain JS objects with TS interfaces/types over classes. This aligns better with React's functional paradigm and data flow.
*   **ES Modules:** Use `import`/`export` for encapsulation. Avoid "private" class members; instead, keep internal functions unexported within a module.
*   **Type Safety:**
    *   **Avoid `any`:** Strictly avoid `any`. Use `unknown` with type narrowing if the type is truly dynamic.
    *   **Type Assertions:** Use `as Type` sparingly and only when necessary (e.g., known external library issues).
*   **Switch Statements:** Use `checkExhaustive` (or similar pattern) in `default` clauses to ensure all cases are handled.
*   **Array Operators:** Prefer immutable array methods (`map`, `filter`, `reduce`) over imperative loops to promote functional patterns and readability.

### React Best Practices
*   **Functional Components & Hooks:** Use functional components exclusively. Manage state with `useState`/`useReducer` and side effects with `useEffect`.
*   **Pure Rendering:** Render logic must be pure. No side effects (network calls, mutations) in the render body.
*   **One-Way Data Flow:** Pass data down via props. Lift state up or use Context for shared data. Avoid syncing local state manually.
*   **Immutability:** Never mutate state directly (e.g., `state.value = 1`). Use state setters (e.g., `setState(prev => ...)`).
*   **useEffect Discipline:** Use `useEffect` primarily for synchronization. Avoid it for derived state or user event handling. Always define strict dependency arrays.
*   **Concurrency:** Write components that are resilient to multiple renders.
*   **UX/UI:** Provide clear loading states (skeletons over spinners) and error handling.

### Testing Guidelines
*   **Framework:** Vitest is the preferred framework.
*   **Structure:** Co-locate test files (`*.test.tsx`) with source files.
*   **Mocking:** Use `vi.mock` for dependencies. Place critical mocks at the very top of the file.
*   **Async:** Use `async/await` and `vi.useFakeTimers()` for time-dependent logic.

### Logging & Comments
*   **Comments:** Only add high-value comments that explain *why*, not *what*.
*   **Logging:** Avoid `console.log` in production code. Use appropriate logging utilities if available.