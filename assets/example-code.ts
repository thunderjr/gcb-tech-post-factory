interface IExample {}
interface IDependency {}

class NiceExampleClass implements IExample {
  constructor(private readonly niceDependency: IDependency) {}

  public async niceMethod(): Promise<Record<string, string>> {
    return {
      "key": "GCB Tech 🚀"
    };
  }
}