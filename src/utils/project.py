__all__ = ["PartialProject","Project"]

class PartialProject:
  def __init__(self,name,repo_url,*args,polling=False,commit="None",**kwargs):
    self.name = name
    self.repo_url = repo_url # repo url should be in format of `https://www.github.com/`
    self.commit = commit
    self.date = 0 # Unix timestamp of commit
    self.polling = polling

  async def get_info(self,session):
    # Only required for polling type projects
    pass

  @property
  def as_dict(self):
    return {
      "name":self.name,
      "commit":self.commit,
      "repo_url":self.repo_url,
      "polling":self.polling,
    }

  @classmethod
  def from_dict(cls,d):
    return cls(
      d["name"],
      d["repo_url"],
      polling=d["polling"],
      commit=d["commit"]
    )

class Project(PartialProject):
  def __init__(self,*args,**kwargs):
    super().__init__(*args,**kwargs)
    self.location = kwargs.get("location",None)
    self.during = kwargs.get("during","default.sh") # default.sh will be just standard `git clone`
    self.before = kwargs.get("before",None)
    self.after = kwargs.get("after",None)