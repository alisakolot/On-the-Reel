--
-- PostgreSQL database dump
--

-- Dumped from database version 10.12 (Ubuntu 10.12-0ubuntu0.18.04.1)
-- Dumped by pg_dump version 10.12 (Ubuntu 10.12-0ubuntu0.18.04.1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: following; Type: TABLE; Schema: public; Owner: vagrant
--

CREATE TABLE public.following (
    following_id integer NOT NULL,
    creator_id integer,
    subscriber_id integer
);


ALTER TABLE public.following OWNER TO vagrant;

--
-- Name: following_following_id_seq; Type: SEQUENCE; Schema: public; Owner: vagrant
--

CREATE SEQUENCE public.following_following_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.following_following_id_seq OWNER TO vagrant;

--
-- Name: following_following_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: vagrant
--

ALTER SEQUENCE public.following_following_id_seq OWNED BY public.following.following_id;


--
-- Name: image; Type: TABLE; Schema: public; Owner: vagrant
--

CREATE TABLE public.image (
    image_id integer NOT NULL,
    image_path character varying,
    description text,
    date_posted timestamp without time zone
);


ALTER TABLE public.image OWNER TO vagrant;

--
-- Name: image_image_id_seq; Type: SEQUENCE; Schema: public; Owner: vagrant
--

CREATE SEQUENCE public.image_image_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.image_image_id_seq OWNER TO vagrant;

--
-- Name: image_image_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: vagrant
--

ALTER SEQUENCE public.image_image_id_seq OWNED BY public.image.image_id;


--
-- Name: reaction; Type: TABLE; Schema: public; Owner: vagrant
--

CREATE TABLE public.reaction (
    reaction_id integer NOT NULL,
    reaction integer,
    video_id integer,
    image_id integer,
    user_id integer
);


ALTER TABLE public.reaction OWNER TO vagrant;

--
-- Name: reaction_reaction_id_seq; Type: SEQUENCE; Schema: public; Owner: vagrant
--

CREATE SEQUENCE public.reaction_reaction_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.reaction_reaction_id_seq OWNER TO vagrant;

--
-- Name: reaction_reaction_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: vagrant
--

ALTER SEQUENCE public.reaction_reaction_id_seq OWNED BY public.reaction.reaction_id;


--
-- Name: users; Type: TABLE; Schema: public; Owner: vagrant
--

CREATE TABLE public.users (
    user_id integer NOT NULL,
    username character varying,
    first_name character varying,
    last_name character varying,
    email character varying,
    password character varying
);


ALTER TABLE public.users OWNER TO vagrant;

--
-- Name: users_user_id_seq; Type: SEQUENCE; Schema: public; Owner: vagrant
--

CREATE SEQUENCE public.users_user_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.users_user_id_seq OWNER TO vagrant;

--
-- Name: users_user_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: vagrant
--

ALTER SEQUENCE public.users_user_id_seq OWNED BY public.users.user_id;


--
-- Name: video; Type: TABLE; Schema: public; Owner: vagrant
--

CREATE TABLE public.video (
    video_id integer NOT NULL,
    video_path character varying,
    description text,
    date_posted timestamp without time zone
);


ALTER TABLE public.video OWNER TO vagrant;

--
-- Name: video_video_id_seq; Type: SEQUENCE; Schema: public; Owner: vagrant
--

CREATE SEQUENCE public.video_video_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.video_video_id_seq OWNER TO vagrant;

--
-- Name: video_video_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: vagrant
--

ALTER SEQUENCE public.video_video_id_seq OWNED BY public.video.video_id;


--
-- Name: following following_id; Type: DEFAULT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY public.following ALTER COLUMN following_id SET DEFAULT nextval('public.following_following_id_seq'::regclass);


--
-- Name: image image_id; Type: DEFAULT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY public.image ALTER COLUMN image_id SET DEFAULT nextval('public.image_image_id_seq'::regclass);


--
-- Name: reaction reaction_id; Type: DEFAULT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY public.reaction ALTER COLUMN reaction_id SET DEFAULT nextval('public.reaction_reaction_id_seq'::regclass);


--
-- Name: users user_id; Type: DEFAULT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY public.users ALTER COLUMN user_id SET DEFAULT nextval('public.users_user_id_seq'::regclass);


--
-- Name: video video_id; Type: DEFAULT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY public.video ALTER COLUMN video_id SET DEFAULT nextval('public.video_video_id_seq'::regclass);


--
-- Data for Name: following; Type: TABLE DATA; Schema: public; Owner: vagrant
--

COPY public.following (following_id, creator_id, subscriber_id) FROM stdin;
1	5	3
2	5	3
3	6	4
\.


--
-- Data for Name: image; Type: TABLE DATA; Schema: public; Owner: vagrant
--

COPY public.image (image_id, image_path, description, date_posted) FROM stdin;
1	path string1	ABCD	2020-08-19 01:41:28.192391
2	pathstring2	EFGH	2020-08-19 01:41:28.192416
3	\N	https://res.cloudinary.com/hb-project/image/upload/v1597879799/gqlmacobspzpeqxffg5y.jpg	\N
4	\N	https://res.cloudinary.com/hb-project/image/upload/v1597879825/ihowg5536n37csqga13t.jpg	\N
5	\N	https://res.cloudinary.com/hb-project/image/upload/v1597879977/ajkdyqovrgcdojf9527o.jpg	\N
6	\N	https://res.cloudinary.com/hb-project/image/upload/v1597880031/ylsfstx14jsak6sbdu6d.jpg	\N
7	\N	https://res.cloudinary.com/hb-project/image/upload/v1597881018/q54m75zdx3vfvw01dj3g.jpg	\N
8	https://res.cloudinary.com/hb-project/image/upload/v1597881196/picjrnqjacbrafuhkxdz.heic	https://res.cloudinary.com/hb-project/image/upload/v1597881196/picjrnqjacbrafuhkxdz.heic	\N
9	https://res.cloudinary.com/hb-project/image/upload/v1597881381/nv6szmj9nlrtowngrdax.heic	\N	\N
10	https://res.cloudinary.com/hb-project/image/upload/v1597881578/mk6ityxriixghxvdapty.heic	prarie with flowers	\N
11	https://res.cloudinary.com/hb-project/image/upload/v1597950555/wv3vrxvvvlkvwxtekq4u.jpg		\N
12	https://res.cloudinary.com/hb-project/image/upload/v1597967238/qroix96ivypkwt0rtamc.gif		\N
13	https://res.cloudinary.com/hb-project/image/upload/v1597967406/zpcmgxjhgtzdvzns9psh.jpg		\N
14	https://res.cloudinary.com/hb-project/image/upload/v1597967442/zzj3oi2ibag1q8amfmzn.jpg		\N
15	https://res.cloudinary.com/hb-project/image/upload/v1597967453/iywqslzeiv2wea6kr9x1.jpg		\N
16	https://res.cloudinary.com/hb-project/image/upload/v1597967477/uvdclurwi6zfkcmcxuh1.jpg		\N
17	https://res.cloudinary.com/hb-project/image/upload/v1597967499/mpxgex8uvnfc4zb9rgkr.jpg		\N
18	https://res.cloudinary.com/hb-project/image/upload/v1597967754/w32ckpv6no8bwxpr0zwi.jpg		\N
19	https://res.cloudinary.com/hb-project/image/upload/v1597967822/esjpp8fkisumesxiqlz8.jpg		\N
20	https://res.cloudinary.com/hb-project/image/upload/v1597967872/mrybgm1ala2oxygh0vto.jpg		\N
21	https://res.cloudinary.com/hb-project/image/upload/v1597967909/oup1jkd7lr1g5zooz7u1.jpg		\N
22	https://res.cloudinary.com/hb-project/image/upload/v1597968044/xt9kgrunzyj0hdookp1t.jpg		\N
23	https://res.cloudinary.com/hb-project/image/upload/v1597968218/c5am1hveinihumqj57y0.jpg		\N
24	https://res.cloudinary.com/hb-project/image/upload/v1597968832/jqdgr6lx6ggzwyi5fpbq.jpg		\N
25	https://res.cloudinary.com/hb-project/image/upload/v1597968926/rwhxh1cjv3qycv5zgt7j.jpg		\N
26	https://res.cloudinary.com/hb-project/image/upload/v1598045614/rctpst4ciiz2ikkn7jkf.jpg		\N
\.


--
-- Data for Name: reaction; Type: TABLE DATA; Schema: public; Owner: vagrant
--

COPY public.reaction (reaction_id, reaction, video_id, image_id, user_id) FROM stdin;
1	1	2	\N	5
2	4	2	\N	2
3	2	2	\N	3
4	5	2	\N	6
5	3	2	\N	2
6	4	\N	1	6
7	3	\N	2	6
8	3	\N	1	4
9	2	\N	2	6
10	4	\N	1	2
\.


--
-- Data for Name: users; Type: TABLE DATA; Schema: public; Owner: vagrant
--

COPY public.users (user_id, username, first_name, last_name, email, password) FROM stdin;
1	alisak	alisa 	kolot	\N	\N
2	username	first_name	last_name	user0@test.com	test
3	username	first_name	last_name	user1@test.com	test
4	username	first_name	last_name	user2@test.com	test
5	username	first_name	last_name	user3@test.com	test
6	username	first_name	last_name	user4@test.com	test
7	test1	test	testtest	test@test	test
8	us	ak	lk	\N	\N
9	un	ak	lk	\N	\N
10	lk	ak	lk	\N	\N
11	finlan	fin	lan	fin@fin	password
12	purplerain	purple	rain	purplerain@rain	purple
13	bob1	bob	bobert	bob@bob	password1
14	kiwibird1	Ki	Wi	kiwi@kiwi	kiwi
\.


--
-- Data for Name: video; Type: TABLE DATA; Schema: public; Owner: vagrant
--

COPY public.video (video_id, video_path, description, date_posted) FROM stdin;
1	path string1	abcd	2020-08-19 01:41:28.184557
2	pathstring2	efgh	2020-08-19 01:41:28.192318
\.


--
-- Name: following_following_id_seq; Type: SEQUENCE SET; Schema: public; Owner: vagrant
--

SELECT pg_catalog.setval('public.following_following_id_seq', 3, true);


--
-- Name: image_image_id_seq; Type: SEQUENCE SET; Schema: public; Owner: vagrant
--

SELECT pg_catalog.setval('public.image_image_id_seq', 26, true);


--
-- Name: reaction_reaction_id_seq; Type: SEQUENCE SET; Schema: public; Owner: vagrant
--

SELECT pg_catalog.setval('public.reaction_reaction_id_seq', 10, true);


--
-- Name: users_user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: vagrant
--

SELECT pg_catalog.setval('public.users_user_id_seq', 14, true);


--
-- Name: video_video_id_seq; Type: SEQUENCE SET; Schema: public; Owner: vagrant
--

SELECT pg_catalog.setval('public.video_video_id_seq', 2, true);


--
-- Name: following following_pkey; Type: CONSTRAINT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY public.following
    ADD CONSTRAINT following_pkey PRIMARY KEY (following_id);


--
-- Name: image image_pkey; Type: CONSTRAINT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY public.image
    ADD CONSTRAINT image_pkey PRIMARY KEY (image_id);


--
-- Name: reaction reaction_pkey; Type: CONSTRAINT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY public.reaction
    ADD CONSTRAINT reaction_pkey PRIMARY KEY (reaction_id);


--
-- Name: users users_email_key; Type: CONSTRAINT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_email_key UNIQUE (email);


--
-- Name: users users_pkey; Type: CONSTRAINT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_pkey PRIMARY KEY (user_id);


--
-- Name: video video_pkey; Type: CONSTRAINT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY public.video
    ADD CONSTRAINT video_pkey PRIMARY KEY (video_id);


--
-- Name: following following_creator_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY public.following
    ADD CONSTRAINT following_creator_id_fkey FOREIGN KEY (creator_id) REFERENCES public.users(user_id);


--
-- Name: following following_subscriber_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY public.following
    ADD CONSTRAINT following_subscriber_id_fkey FOREIGN KEY (subscriber_id) REFERENCES public.users(user_id);


--
-- Name: reaction reaction_image_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY public.reaction
    ADD CONSTRAINT reaction_image_id_fkey FOREIGN KEY (image_id) REFERENCES public.image(image_id);


--
-- Name: reaction reaction_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY public.reaction
    ADD CONSTRAINT reaction_user_id_fkey FOREIGN KEY (user_id) REFERENCES public.users(user_id);


--
-- Name: reaction reaction_video_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY public.reaction
    ADD CONSTRAINT reaction_video_id_fkey FOREIGN KEY (video_id) REFERENCES public.video(video_id);


--
-- PostgreSQL database dump complete
--

