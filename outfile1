
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
    date_posted timestamp without time zone,
    user_id integer
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
1	4	2
2	2	1
3	3	4
4	4	5
5	4	6
6	7	6
7	4	6
8	7	1
9	6	1
10	6	1
11	8	7
12	7	8
13	6	8
14	8	6
15	8	9
18	9	8
19	10	8
24	9	11
25	11	8
\.


--
-- Data for Name: image; Type: TABLE DATA; Schema: public; Owner: vagrant
--

COPY public.image (image_id, image_path, description, date_posted, user_id) FROM stdin;
1	path string1	ABCD	2020-08-21 23:07:35.048323	4
2	pathstring2	EFGH	2020-08-21 23:07:35.056595	4
30	https://res.cloudinary.com/hb-project/image/upload/v1598315598/uhss390aklzimziogpjc.jpg		\N	6
31	https://res.cloudinary.com/hb-project/image/upload/v1598390201/dzkrtun7czu8dfxwmvu0.jpg		\N	6
32	https://res.cloudinary.com/hb-project/image/upload/v1598390248/mnm99gt97wmywrzxfm7b.jpg		\N	6
33	https://res.cloudinary.com/hb-project/image/upload/v1598390298/iimnf7wimrebsshgeaun.jpg		\N	6
34	https://res.cloudinary.com/hb-project/image/upload/v1598390526/pqlztcbfep4greaez39d.jpg		\N	6
35	https://res.cloudinary.com/hb-project/image/upload/v1598390664/p7f9jpst6yyqy1rnaajx.jpg		\N	6
36	https://res.cloudinary.com/hb-project/image/upload/v1598390778/cfbjoisggnism9q2tgh0.jpg		\N	6
37	https://res.cloudinary.com/hb-project/image/upload/v1598390874/z9s71ouxdzsdvhsvxhtz.jpg		\N	6
38	https://res.cloudinary.com/hb-project/image/upload/v1598391114/wfbkx9w9ofu8xkfguxao.jpg		\N	6
39	https://res.cloudinary.com/hb-project/image/upload/v1598391121/wunrxduy4wthc8ejsxal.jpg		\N	6
40	https://res.cloudinary.com/hb-project/image/upload/v1598391143/lniwxepfs4vtveussgi3.gif		\N	6
41	https://res.cloudinary.com/hb-project/image/upload/v1598391418/awdh5tq3v25ireijfmok.jpg		\N	6
42	https://res.cloudinary.com/hb-project/image/upload/v1598391443/hfww20wnf2sxenunuf7s.jpg		\N	6
43	https://res.cloudinary.com/hb-project/image/upload/v1598391453/vcujqr2wtmp7g3oys9ie.jpg		\N	6
44	https://res.cloudinary.com/hb-project/image/upload/v1598392192/erfi5yeahsqlnok1ol3v.jpg		\N	6
45	https://res.cloudinary.com/hb-project/image/upload/v1598392243/ifgardpefwb62foikpi1.jpg		\N	6
46	https://res.cloudinary.com/hb-project/image/upload/v1598392267/kiluvwngu1ql7govjte7.jpg		\N	6
47	https://res.cloudinary.com/hb-project/image/upload/v1598392369/mbiek1kixuzuqhswhopx.jpg		\N	6
48	https://res.cloudinary.com/hb-project/image/upload/v1598392415/ezgj4yrlzjohowcjghrh.jpg		\N	6
49	https://res.cloudinary.com/hb-project/image/upload/v1598392482/dur9junwlzhl9ad0qkxn.jpg		\N	6
50	https://res.cloudinary.com/hb-project/image/upload/v1598392635/hhpwjdcv4ift3d6guyu5.jpg		\N	6
51	https://res.cloudinary.com/hb-project/image/upload/v1598392821/hysp5nykcuh7i42wpso4.jpg		\N	6
52	https://res.cloudinary.com/hb-project/image/upload/v1598403338/h7yghjnaoerpfgrrigzk.jpg		\N	7
53	https://res.cloudinary.com/hb-project/image/upload/v1598403364/c7gfejogpbawrpbgvdjs.gif	running kiwi	\N	7
54	https://res.cloudinary.com/hb-project/image/upload/v1599000632/fbvf1kn5r1ql8ukdbvbo.jpg		\N	8
3	https://res.cloudinary.com/hb-project/image/upload/v1598051742/sdlenavnpqhzlml6puim.jpg	kiwi: is hold	\N	1
4	https://res.cloudinary.com/hb-project/image/upload/v1598054306/ch8lpaz6edlxwxrwapmw.jpg		\N	1
5	https://res.cloudinary.com/hb-project/image/upload/v1598205353/gbk0vsh4zt4s57krcuxm.jpg	kiwi, little spotted 	\N	1
6	https://res.cloudinary.com/hb-project/image/upload/v1598207222/flqpggwd7rfbatkyerq7.jpg		\N	1
7	https://res.cloudinary.com/hb-project/image/upload/v1598207440/fazgb708rifzn2wzjhth.jpg		\N	1
8	https://res.cloudinary.com/hb-project/image/upload/v1598207468/czqivprimeoikh28v7ip.jpg		\N	1
9	https://res.cloudinary.com/hb-project/image/upload/v1598207761/uvqdmhsdgcsbnx6blmn4.jpg		\N	1
10	https://res.cloudinary.com/hb-project/image/upload/v1598208526/f3zzaxosd3ar5enhslt0.jpg		\N	1
11	https://res.cloudinary.com/hb-project/image/upload/v1598211689/ohd1hnlbbnuuil68w7ks.jpg		\N	1
12	https://res.cloudinary.com/hb-project/image/upload/v1598214992/z0r1urcgdmndmz2rojyv.jpg		\N	1
13	https://res.cloudinary.com/hb-project/image/upload/v1598215478/dlsukpw2ppuaxwcnjrl4.jpg		\N	1
14	https://res.cloudinary.com/hb-project/image/upload/v1598215535/mf6tutin7aajjzwofej1.jpg		\N	1
15	https://res.cloudinary.com/hb-project/image/upload/v1598216100/euj16msgitzt6w4tfgan.jpg		\N	1
16	https://res.cloudinary.com/hb-project/image/upload/v1598216211/kediaufxorts1rswmss1.jpg	random	\N	1
17	https://res.cloudinary.com/hb-project/image/upload/v1598224674/cnbfdbm0t4mzmwjlpnnh.jpg		\N	1
18	https://res.cloudinary.com/hb-project/image/upload/v1598224892/wdz1rir67dsutdumoynj.jpg		\N	1
19	https://res.cloudinary.com/hb-project/image/upload/v1598229166/lxyusufkuixeguxrfgnb.jpg		\N	1
20	https://res.cloudinary.com/hb-project/image/upload/v1598238647/sjj6pqaqmjxajrvgjtrq.jpg		\N	1
21	https://res.cloudinary.com/hb-project/image/upload/v1598239026/yz0dsvkeb8j5tdw0zzz1.jpg		\N	1
22	https://res.cloudinary.com/hb-project/image/upload/v1598239665/cmqehxdgvdih7kyrpmkf.jpg		\N	1
23	https://res.cloudinary.com/hb-project/image/upload/v1598309952/jqwn7ex223z5u89jndeb.jpg		\N	1
24	https://res.cloudinary.com/hb-project/image/upload/v1598314591/hhipzucqybwygxkp9bov.jpg		\N	1
25	https://res.cloudinary.com/hb-project/image/upload/v1598314657/fe4ceumpts73q5fkxrbe.jpg		\N	1
26	https://res.cloudinary.com/hb-project/image/upload/v1598315065/w0nl4k6epycea4lxfel9.jpg		\N	1
27	https://res.cloudinary.com/hb-project/image/upload/v1598315135/xqk07nncq6zvn9ymxmuv.jpg		\N	1
28	https://res.cloudinary.com/hb-project/image/upload/v1598315326/rb9kuxysplpvg8xdur8w.jpg		\N	1
29	https://res.cloudinary.com/hb-project/image/upload/v1598315437/zhttt45ckof9jljycxzt.jpg		\N	1
55	https://res.cloudinary.com/hb-project/image/upload/v1599008551/avdga8r7huzrb6wxyz5z.jpg		\N	6
56	https://res.cloudinary.com/hb-project/image/upload/v1599008754/qr8eme8hggkopilybrhe.jpg		\N	6
57	https://res.cloudinary.com/hb-project/image/upload/v1599008821/tev09oiwlyw1qs4fvw4m.jpg		\N	9
58	https://res.cloudinary.com/hb-project/image/upload/v1599075363/etfcb7gjnkactpgwdiwl.jpg	ash tree	\N	10
59	https://res.cloudinary.com/hb-project/image/upload/v1599075518/y9uqpghzg4tvpsuynn5x.gif	kiwi gif	\N	10
60	https://res.cloudinary.com/hb-project/image/upload/v1599092308/x6rlkvisgoaftqrw71ca.jpg	my future mountain trip 	\N	11
\.


--
-- Data for Name: reaction; Type: TABLE DATA; Schema: public; Owner: vagrant
--

COPY public.reaction (reaction_id, reaction, video_id, image_id, user_id) FROM stdin;
1	5	1	\N	4
2	3	1	\N	2
3	3	1	\N	3
4	5	2	\N	2
5	1	1	\N	4
6	1	\N	2	3
7	4	\N	2	2
8	5	\N	1	2
9	3	\N	2	5
10	4	\N	1	4
11	4	\N	\N	6
12	2	\N	1	6
13	1	\N	3	6
14	1	\N	52	6
15	2	\N	51	1
16	3	\N	54	6
17	1	\N	54	6
18	2	\N	54	9
19	1	\N	57	10
20	3	\N	57	10
21	1	\N	59	11
22	3	\N	57	11
23	2	\N	57	11
24	1	\N	57	11
\.


--
-- Data for Name: users; Type: TABLE DATA; Schema: public; Owner: vagrant
--

COPY public.users (user_id, username, first_name, last_name, email, password) FROM stdin;
1	username	first_name	last_name	user0@test.com	test
2	username	first_name	last_name	user1@test.com	test
3	username	first_name	last_name	user2@test.com	test
4	username	first_name	last_name	user3@test.com	test
5	username	first_name	last_name	user4@test.com	test
6	kiwi1	Kiwi	Zealand	kiwi@kiwi	kiwi
7	kiwi-cat	Kiwi	Cat	kiwicat@gmail.com	kiwi
8	ada1	Ada	Lovelace	ada@ada	ada
9	lisafrank	Lisa	Frank	lisa@lisa	password
10	natasha	natalia	jadan	nata66a@gmail.com	password
11	skosha	sasha	kosha	o5255@yahoo.com	password
\.


--
-- Data for Name: video; Type: TABLE DATA; Schema: public; Owner: vagrant
--

COPY public.video (video_id, video_path, description, date_posted) FROM stdin;
1	path string1	abcd	2020-08-21 23:07:28.794438
2	pathstring2	efgh	2020-08-21 23:07:28.794467
\.


--
-- Name: following_following_id_seq; Type: SEQUENCE SET; Schema: public; Owner: vagrant
--

SELECT pg_catalog.setval('public.following_following_id_seq', 25, true);


--
-- Name: image_image_id_seq; Type: SEQUENCE SET; Schema: public; Owner: vagrant
--

SELECT pg_catalog.setval('public.image_image_id_seq', 60, true);


--
-- Name: reaction_reaction_id_seq; Type: SEQUENCE SET; Schema: public; Owner: vagrant
--

SELECT pg_catalog.setval('public.reaction_reaction_id_seq', 24, true);


--
-- Name: users_user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: vagrant
--

SELECT pg_catalog.setval('public.users_user_id_seq', 11, true);


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
-- Name: image image_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY public.image
    ADD CONSTRAINT image_user_id_fkey FOREIGN KEY (user_id) REFERENCES public.users(user_id);


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

