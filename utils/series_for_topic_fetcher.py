from podcasts.top_series_for_topic import fetch_series_all_genres

def generate_series_for_topic_models(current_entries):
  topics_to_series = dict(fetch_series_all_genres())
  existing_topics = set([e.get('topic_id') for e in current_entries])
  nonexisting_topics = \
    set(topics_to_series.keys()) - existing_topics
  inserts = [
      {
          'topic_id': tid,
          'series_list': ','.join(map(str, topics_to_series[tid]))
      }
      for tid in nonexisting_topics
  ]
  updates = [
      {
          'topic_id': tid,
          'series_list': ','.join(map(str, topics_to_series[tid]))
      }
      for tid in existing_topics
  ]
  return inserts, updates
