# notion-charts

![image](/example.png)

## Usage

### For non-private notions

Simply use https://notion-charts.now.sh url, and follow the documentation below.

### For private notions

You'll need to host your own version of this repository.
The best way to do that is by clicking this button bellow, it will automatically host this API on [zeit.co](https://zeit.co/) which is **100% free**.

<details>
  <summary>Show me the steps</summary>

  1. Click the blue **Deploy** button on this page
  2. Zeit is now opened, click **Continue**
  2. Then if you don't already have an account click **Sign Up** in the top right corner
  3. Choose a name for your project, keep in mind that this name will goes in your url `https://YOUR-PROJECT-NAME.now.sh`
  4. Don't forget to put your notion `TOKEN_V2` before clicking **Continue** [If you don't know how to get it, click here](/notion-token.md)
  5. Click **Continue** one more time, and you're done!

</details>

Then when the hosting is completed simply follow documentation instructions below and enjoy 😎

[![Deploy with ZEIT Now](https://zeit.co/button)](https://zeit.co/import/project?template=https://github.com/mathix420/notion-charts)


## Documentation

### Image charts

```
/chart-image/<collection>/<view>
```
Example:

> https://www.notion.so/fa9b093633c0479f886fdb857f57f9b0?v=c94a0043c3df410cb461e7698cee6aff
>
> => https://notion-charts.now.sh/chart-image/fa9b093633c0479f886fdb857f57f9b0/c94a0043c3df410cb461e7698cee6aff

### Interactive charts

```
/chart/<collection>/<view>
```
Examples:

> https://www.notion.so/fa9b093633c0479f886fdb857f57f9b0?v=c94a0043c3df410cb461e7698cee6aff
>
> => https://notion-charts.now.sh/chart/fa9b093633c0479f886fdb857f57f9b0/c94a0043c3df410cb461e7698cee6aff


> https://www.notion.so/fa9b093633c0479f886fdb857f57f9b0?v=f1b7adb289cc4da3aa7ee6b8ac68470e
>
> => https://notion-charts.now.sh/chart/fa9b093633c0479f886fdb857f57f9b0/f1b7adb289cc4da3aa7ee6b8ac68470e

## Open for contributions

I know this API is not very flexible, but if someone want to make it better I'd be glad to accept its contribution.
