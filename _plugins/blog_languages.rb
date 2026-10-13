# One source post, two crawlable language editions. Translations are pages,
# not posts, so lists, counts, archives and feeds retain a single entry.
module ResearchBlog
  class Languages < Jekyll::Generator
    safe true
    priority :high

    def generate(site)
      site.posts.docs.each do |post|
        next unless post.data['layout'] == 'blog-post'
        korean = post.data['korean']
        next unless korean.is_a?(Hash) && post.content.include?('<!-- lang:ko -->')

        english = { 'title' => post.data['title'], 'description' => post.data['description'] }
        english_url = post.url
        korean_url = "#{english_url}ko/"
        post.data.merge!('english' => english, 'english_url' => english_url, 'korean_url' => korean_url)

        edition = Jekyll::PageWithoutAFile.new(site, site.source, korean_url.sub(%r{^/}, ''), 'index.md')
        edition.content = post.content
        edition.data = post.data.merge(
          'title' => korean['title'], 'description' => korean['description'],
          'lang' => 'ko', 'permalink' => korean_url, 'sitemap' => true,
          'english' => english, 'english_url' => english_url, 'korean_url' => korean_url
        )
        site.pages << edition
      end
    end
  end
end
