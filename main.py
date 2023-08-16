"""
This Add-On allows users to add tags or key/value pairs in bulk.
"""

from documentcloud.addon import AddOn

class BulkTag(AddOn):
    """An example Add-On for DocumentCloud."""

    def main(self):
        """The main add-on functionality goes here."""
        # fetch your add-on specific data
        key = self.data.get("key")
        value = self.data.get("value")
    
        for document in self.get_documents():
            if document.data.has_key(key):
                document.data[key].append(value)
                document.save()
            else:
                document.data[key] = value
                document.save()


if __name__ == "__main__":
    BulkTag().main()
