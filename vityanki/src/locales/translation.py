import yaml
from pathlib import Path
from logger import setup_logging
import os

logger = setup_logging('translations')

# Load all translation files on startup
INTERFACE_TRANSLATIONS = {}

locales_dir = os.path.join(os.getcwd(), "vityanki", "src", "locales")
if not os.path.exists(locales_dir):
    logger.error(f"Locales directory '{locales_dir}' does not exist.")
else:
    logger.info(f"Loading translations from directory: {locales_dir}")
    
for filename in os.listdir(locales_dir):
    if filename.endswith(".yaml"):
        language_code = os.path.splitext(filename)[0]
        file_path = os.path.join(locales_dir, filename)
        with open(file_path, 'r', encoding='utf-8') as f:
            INTERFACE_TRANSLATIONS[language_code] = yaml.safe_load(f)

def t(language, key):
    """
    Retrieves the translation for a given dotted key string and language, with fallback to English.
    Args:
        language (str): The language code to retrieve the translation for (e.g., 'en', 'fr').
        key (str): The dotted key string representing the translation path (e.g., 'menu.file.open').
    Returns:
        str: The translated string if found for the specified language or English; otherwise, returns the key itself.
    Example:
        >>> t('fr', 'menu.file.open')
        'Ouvrir le fichier'
        >>> t('es', 'menu.file.save')
        'Guardar archivo'
        >>> t('xx', 'menu.file.exit')
        'Exit'  # Fallback to English
        >>> t('en', 'nonexistent.key')
        'nonexistent.key'  # Key not found in any language
    """
    def get_nested(dictionary, path):
        """
        Retrieves a value from a nested dictionary using a dot-delimited key path.
        Args:
            dictionary (dict): The nested dictionary to search in.
            path (str): The dot-separated key path representing the hierarchy 
                        (e.g., "menu.file.open").
        Returns:
            Any: The value found at the nested key path, or None if any part of the path is missing.
        Example:
            >>> data = {
            ...     "menu": {
            ...         "file": {
            ...             "open": "Open File"
            ...         }
            ...     }
            ... }
            >>> get_nested(data, "menu.file.open")
            'Open File'

            >>> get_nested(data, "menu.file.save")
            None  # "save" key does not exist
        """
        for part in path.split("."):
            dictionary = dictionary.get(part)
            if dictionary is None:
                return None
        return dictionary

    result = get_nested(INTERFACE_TRANSLATIONS.get(language, {}), key)
    if result is not None:
        return result
    elif get_nested(INTERFACE_TRANSLATIONS.get("en", {}), key):
        # Fallback to English if the key exists in English
        logger.info(f"Translation for '{key}' not found in '{language}', falling back to English.")
        return get_nested(INTERFACE_TRANSLATIONS.get("en", {}), key)
    else:
        logger.info(f"Translation for '{key}' not found in any language, returning the key itself.")
        return key
