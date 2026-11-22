from typing import Any, Dict, List


class SearchIndexTools:
    def __init__(self, index: Any) -> None:
        self.index = index

    def search(self, query: str) -> List[Dict[str, Any]]:
        """
        Search the documentation database for relevant results based on a query string.

        Args:
            query (str): The search query to look up in the index.

        Returns:
            List[Dict[str, Any]]: A list of search result objects returned by the index.
        """
        results = self.index.search(
            query=query,
            num_results=5
        )
        return results

    def add_entry(
        self,
        filename: str,
        title: str,
        description: str,
        content: str
    ) -> str:
        """
        Add a new documentation entry to the index.

        Args:
            filename (str): The source filename associated with the entry.
            title (str): The title of the documentation entry.
            description (str): A short description summarizing the entry.
            content (str): The full content of the documentation entry.

        Returns:
            str: A status message indicating the result of the operation ("OK").
        """
        entry: Dict[str, Any] = {
            "start": 0,
            "content": content,
            "title": title,
            "description": description,
            "filename": filename,
        }
        self.index.append(entry)
        return "OK"


class SearchTools:
    """Search + get_file tools over full docs (going beyond RAG / PydanticAI)."""

    def __init__(self, index: Any, highlighter: Any, file_index: Dict[str, str]) -> None:
        self.index = index
        self.highlighter = highlighter
        self.file_index = file_index

    def search(self, query: str) -> List[Dict[str, Any]]:
        """
        Search the documentation database and return highlighted snippets.

        Args:
            query: The search query to look up in the index.

        Returns:
            Matching documents with short highlighted snippets.
        """
        search_results = self.index.search(query=query, num_results=5)
        return self.highlighter.highlight(query, search_results)

    def get_file(self, filename: str) -> str:
        """
        Retrieve the full contents of a documentation file.

        Args:
            filename: The filename to retrieve.

        Returns:
            The full file contents, or an error message if the file is missing.
        """
        if filename in self.file_index:
            return self.file_index[filename]
        return f"file {filename} does not exist"
