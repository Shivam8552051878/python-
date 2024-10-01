import hashlib

class URLShortener:
    def __init__(self):
        self.url_map = {}

    def shorten_url(self, long_url):
        # Generate a unique identifier for the long URL
        hash_code = hashlib.md5(long_url.encode()).hexdigest()
        short_url = hash_code[:8]  # Take the first 8 characters as the short URL
        
        # Store the mapping between the short URL and the long URL
        self.url_map[short_url] = long_url
        
        return short_url

    def redirect(self, short_url):
        # Redirect to the original URL if it exists in the mapping
        if short_url in self.url_map:
            return self.url_map[short_url]
        else:
            return "URL not found"

# Example usage
url_shortener = URLShortener()
short_url = url_shortener.shorten_url("https://www.example.com")
print("Shortened URL:", short_url)

original_url = url_shortener.redirect(short_url)
print("Original URL:", original_url)
